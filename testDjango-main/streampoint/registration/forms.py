from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from lkusers.models import ContribUsers

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        #fields = '__all__'


# class AddproductForms(forms.ModelForm):
#     class Meta:
#         model = ContribUsers
#         fields = ["telegramm",]


