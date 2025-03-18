from rest_framework import serializers
from blog.models.categorie import Categorie


class CategorieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categorie
        fields = '__all__'
        depth = 1