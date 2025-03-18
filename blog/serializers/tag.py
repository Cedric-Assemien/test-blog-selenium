from rest_framework import serializers
from blog.models.tag import Tag


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'
        depth = 1