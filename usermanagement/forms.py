from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput
from django.forms.fields import DateField
from django.contrib.auth import get_user_model


class DateInputWidget(DateInput):
    input_type = 'date'


class RegisterForm(UserCreationForm):
    birthday = DateField(input_formats=['%Y-%m-%d',
                                        '%m/%d/%Y',
                                        '%m/%d/%y'],
                         label='Geboortedag',
                         widget=DateInputWidget(),
                         required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birthday')
