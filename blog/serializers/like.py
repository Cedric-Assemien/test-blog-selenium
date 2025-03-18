from rest_framework import serializers
from blog.models .like import Like


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'
        depth = 2
