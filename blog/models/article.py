from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.contrib.auth.models import User
import datetime

User = get_user_model()
    

class Article(models.Model):

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    titre = models.CharField(max_length=256)
    couverture = models.ImageField(upload_to="articles")
    resume = models.TextField()
    contenu = RichTextField()

    auteur_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="auteur_article_ids")
    categorie_id = models.ForeignKey('blog.Categorie', on_delete=models.SET_NULL, null=True, related_name="categorie_article_ids", verbose_name="Catégorie")
    tag_ids = models.ManyToManyField('blog.Tag', related_name="tag_article_ids", verbose_name="Tags")
    
    est_publie = models.BooleanField(default=False)
    date_de_publication = models.DateField(default=datetime.date.today)
    slug = models.SlugField(unique=True, blank=True)

    # Standards
    statut = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.titre