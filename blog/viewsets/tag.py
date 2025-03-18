from rest_framework import viewsets
from blog.models.tag import Tag
from blog.serializers.tag import TagSerializer
from rest_framework.permissions import IsAuthenticated
    
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    permission_classes = [IsAuthenticated]