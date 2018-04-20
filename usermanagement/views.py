from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin


class CLoginView(SuccessMessageMixin, LoginView):
    template_name = 'usermanagement/login.html'
    redirect_authenticated_user = 'game'
    success_message = 'You succesfully logged in!'


class CLogoutView(SuccessMessageMixin, LogoutView):
    success_message = 'You successfully logged out!'
    extra_context = {'messages': ['You successfully logged out!']}


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
