from django.contrib import admin
from usermanagement.models import Profile, Members, Contact
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'last_login')
    fieldsets = [
        (None, {'fields': ['username', 'first_name', 'last_name']})
    ]


class MemberInline(admin.TabularInline):
    model = Members
    extra = 0
    verbose_name = 'Member'
    verbose_name_plural = 'Members'


class ContactAdmin(MarkdownxModelAdmin):
    inlines = (MemberInline,)
    readonly_fields = ('created',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Profile, ProfileAdmin)
