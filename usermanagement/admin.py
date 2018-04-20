from django.contrib import admin
from usermanagement.models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'last_login')
    fieldsets = [
        (None, {'fields': ['username', 'first_name', 'last_name']})
    ]


admin.site.register(Profile, ProfileAdmin)
