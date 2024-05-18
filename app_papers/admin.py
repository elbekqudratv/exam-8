from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publication', 'created_at', 'updated_at')
    list_filter = ('status', 'publication')

admin.site.register(Article, ArticleAdmin)
