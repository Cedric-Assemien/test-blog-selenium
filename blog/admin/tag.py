from django.contrib import admin
from blog.models.tag import Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('nom', 'created_at')
    search_fields = ('nom',)
    date_hierarchy = 'created_at'
    ordering = ['nom']
    list_per_page = 10


admin.site.register(Tag, TagAdmin)