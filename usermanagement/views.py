from django.contrib.auth.views import LoginView


class AuthView(LoginView):
    template_name = 'usermanagement/login.html'
