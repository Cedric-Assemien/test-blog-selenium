from rest_framework import viewsets
from blog.models.article import Article
from blog.serializers.article import ArticleSerializer
from rest_framework.permissions import IsAuthenticated


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    permission_classes = [IsAuthenticated]