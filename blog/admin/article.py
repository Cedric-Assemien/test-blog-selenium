from django.contrib import admin
from blog.models.article import Article
from ckeditor.widgets import CKEditorWidget
from django.db import models


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'get_auteur', 'statut', 'created_at', 'last_updated_at')
    list_display_links = ['titre']
    list_filter = ('statut', 'auteur_id')
    search_fields = ('titre', 'contenu', 'auteur_id__username')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 10

    fieldsets = [
        ('Informations principales', {'fields': ['titre', 'contenu', 'auteur_id']}),
        ('Catégorisation', {'fields': ['categorie_id', 'tag_ids']}),
        ('Publication', {'fields': ['est_publie', 'date_de_publication']}),
        ('Standards', {'fields': ['statut']})
    ]

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}  
    }

    actions = ('publier', 'depublier')

    def publier(self, request, queryset):
        queryset.update(est_publie=True)
        self.message_user(request, 'Les articles sélectionnés ont été publiés')
    publier.short_description = 'Publier'

    def depublier(self, request, queryset):
        queryset.update(est_publie=False)
        self.message_user(request, 'Les articles sélectionnés ont été dépubliés')
    depublier.short_description = 'Dépublier'

    def get_auteur(self, obj):
        return obj.auteur_id.username if obj.auteur_id else "Anonyme"
    get_auteur.admin_order_field = 'auteur_id'
    get_auteur.short_description = 'Auteur'
    

admin.site.register(Article, ArticleAdmin)