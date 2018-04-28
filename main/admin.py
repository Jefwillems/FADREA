from django.contrib import admin
from main.models import Article, ArtistImagePost, Artist, ArtistVideoPost, Spotlight
from markdownx.admin import MarkdownxModelAdmin
from main.forms import ArtistVideoAdminForm


# Register your models here.

class ArticleAdmin(MarkdownxModelAdmin):
    readonly_fields = ('created', 'edited')
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


class SpotLightAdmin(admin.ModelAdmin):
    list_display = ('created', 'left_title', 'right_title')
    readonly_fields = ('created', 'edited')
    fieldsets = (
        ('Left', {
            'fields': ('left_title', 'left_image', 'left_url')
        }),
        ('Right', {
            'fields': ('right_title', 'right_image', 'right_url')
        }),
    )


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
admin.site.register(Spotlight, SpotLightAdmin)
