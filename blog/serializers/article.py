from rest_framework import serializers
from blog.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    couverture = serializers.ImageField(required=False)
    categorie = serializers.SerializerMethodField()
    auteur = serializers.SerializerMethodField()  

    class Meta:
        model = Article
        fields = [
            'titre',
            'couverture',
            'resume',
            'contenu',
            'auteur',  
            'categorie',
            'tag_ids',
            'est_publie',
            'slug',
            'created_at'
        ]
        depth = 1

    def get_categorie(self, obj):
        if obj.categorie_id:
            return {"nom": obj.categorie_id.nom}  
        return None

    def get_auteur(self, obj):
        """Retourne seulement le username de l'auteur."""
        return obj.auteur_id.username if obj.auteur_id else None