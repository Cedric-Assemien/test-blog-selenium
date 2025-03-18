from django.contrib import admin
from blog.models.categorie import Categorie


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'statut', 'created_at', 'last_updated_at')
    list_display_links = ['nom']
    list_filter = ('statut',)
    search_fields = ('nom',)
    date_hierarchy = 'created_at'
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        ('Infos', {'fields': ['nom', 'description']}),
        ('Standards', {'fields': ['statut']})
    ]

    actions = ('active', 'desactive')

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, 'La sélection a été activée avec succès')
    active.short_description = 'Activer'

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, 'La sélection a été désactivée avec succès')
    desactive.short_description = 'Désactiver'
    

admin.site.register(Categorie, CategorieAdmin)