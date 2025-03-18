from django.contrib import admin
from blog.models.commentaire import Commentaire

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('get_auteur', 'get_article', 'statut', 'created_at')
    list_display_links = ['get_auteur']
    list_filter = ('statut', 'article_id')
    search_fields = ('auteur_id__username', 'contenu')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    list_per_page = 10

    fieldsets = [
        ('Informations', {'fields': ['auteur_id', 'article_id', 'contenu']}),
        ('Modération', {'fields': ['statut']})
    ]

    actions = ('approuver', 'rejeter')

    def approuver(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'Les commentaires sélectionnés ont été approuvés')
    approuver.short_description = 'Approuver'

    def rejeter(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'Les commentaires sélectionnés ont été rejetés')
    rejeter.short_description = 'Rejeter'

    def get_auteur(self, obj):
        return obj.auteur_id.username if obj.auteur_id else "Anonyme"
    get_auteur.admin_order_field = 'auteur_id'
    get_auteur.short_description = 'Auteur'

    def get_article(self, obj):
        return obj.article_id.titre if obj.article_id else "Sans article"
    get_article.admin_order_field = 'article_id'
    get_article.short_description = 'Article'


admin.site.register(Commentaire, CommentaireAdmin)
