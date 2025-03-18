from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()
    

class Commentaire(models.Model):

    class Meta:
        verbose_name = "Commentaire"
        verbose_name_plural = "Commentaires"

    auteur_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="auteur_commentaire_ids")
    article_id = models.ForeignKey('blog.Article', on_delete=models.CASCADE, related_name="article_commentaire_ids")
    contenu = models.TextField()

    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.auteur_id.username}: {self.contenu[:30]}..."