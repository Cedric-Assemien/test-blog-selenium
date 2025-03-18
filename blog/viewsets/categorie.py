from rest_framework import viewsets
from blog.models.categorie import Categorie
from blog.serializers.categorie import CategorieSerializer
from rest_framework.permissions import IsAuthenticated
   
    
class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer
    
    permission_classes = [IsAuthenticated]