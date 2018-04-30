from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from usermanagement.forms import RegisterForm
from usermanagement.models import Contact


class CLoginView(SuccessMessageMixin, LoginView):
    template_name = 'usermanagement/login.html'
    redirect_authenticated_user = 'game'
    success_message = 'You succesfully logged in!'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'usermanagement/register.html'
    model = get_user_model()


class CLogoutView(LogoutView):
    pass


class CPasswordChangeView(PasswordChangeView):
    pass


class CPasswordChangeDoneView(PasswordChangeDoneView):
    pass


class CPasswordResetView(PasswordResetView):
    pass


class CPasswordResetDoneView(PasswordResetDoneView):
    pass


class CPasswordResetConfirmView(PasswordResetConfirmView):
    pass


class CPasswordResetCompleteView(PasswordResetCompleteView):
    pass


class ContactView(generic.TemplateView):
    template_name = 'usermanagement/contact.html'

    def contact(self):
        return Contact.objects.latest('created')
