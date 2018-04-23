from django.contrib import admin
from main.models import Article
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.

class ArticleAdmin(MarkdownxModelAdmin):
    exclude = ('slug',)


admin.site.register(Article, ArticleAdmin)
