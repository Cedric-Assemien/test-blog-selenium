from rest_framework import viewsets
from blog.models.commentaire import Commentaire
from blog.serializers.commentaire import CommentaireSerializer
from rest_framework.permissions import IsAuthenticated
    
    
class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    
    permission_classes = [IsAuthenticated]