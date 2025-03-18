from rest_framework import viewsets
from blog.models.like import Like
from blog.serializers.like import LikeSerializer
from rest_framework.permissions import IsAuthenticated


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    permission_classes = [IsAuthenticated]