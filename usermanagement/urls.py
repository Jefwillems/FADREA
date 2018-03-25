from django.conf.urls import url

from usermanagement.views import AuthView

urlpatterns = [
    url(r'^login', AuthView.as_view(), name='login'),
]
