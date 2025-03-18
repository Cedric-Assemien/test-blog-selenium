from rest_framework import serializers
from blog.models.commentaire import Commentaire


class CommentaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = Commentaire
        fields = '__all__'
        depth = 2