from django.contrib import admin
from blog.models.like import Like


class LikeAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_article', 'created_at')
    search_fields = ('user_id__username','article_id')
    list_filter = ('article_id',)
    date_hierarchy = 'created_at'
    list_per_page = 10

    def get_user(self, obj):
        return obj.user.username if obj.user else "Anonyme"
    get_user.admin_order_field = 'user'
    get_user.short_description = 'Auteur'

    def get_article(self, obj):
        return obj.article.titre if obj.article else "Sans article"
    get_article.admin_order_field = 'article'
    get_article.short_description = 'Article'


admin.site.register(Like, LikeAdmin)