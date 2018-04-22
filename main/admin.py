from django.contrib import admin
from main.models import Article
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.

class ArticleAdmin(MarkdownxModelAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
