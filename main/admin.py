from django.contrib import admin
from main.models import Article, ArtistImagePost, Artist, ArtistVideoPost
from markdownx.admin import MarkdownxModelAdmin
from main.forms import ArtistVideoAdminForm


# Register your models here.

class ArticleAdmin(MarkdownxModelAdmin):
    exclude = ('slug',)


class ArtistImageInline(admin.TabularInline):
    model = ArtistImagePost
    extra = 0
    exclude = ('slug',)


class ArtistVideoInline(admin.TabularInline):
    model = ArtistVideoPost
    form = ArtistVideoAdminForm
    extra = 0
    exclude = ('slug',)


class PostAdmin(MarkdownxModelAdmin):
    exclude = ('slug', 'edited')


class ArtistAdmin(MarkdownxModelAdmin):
    exclude = ('slug',)


class ArtistImageAdmin(PostAdmin):
    pass


class ArtistVideoAdmin(PostAdmin):
    pass


admin.site.register(Article, ArticleAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(ArtistImagePost, ArtistImageAdmin)
admin.site.register(ArtistVideoPost, ArtistVideoAdmin)
