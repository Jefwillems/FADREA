from django.forms import ModelForm
from markdownx.admin import AdminMarkdownxWidget

from main.models import ArtistVideoPost


class ArtistVideoAdminForm(ModelForm):
    class Meta:
        model = ArtistVideoPost
        widgets = {
            'description': AdminMarkdownxWidget
        }
        fields = '__all__'
