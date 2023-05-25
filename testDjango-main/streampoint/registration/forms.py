from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from lkusers.models import ContribUsers
from django import forms


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class StreamerRegistrationForm(UserCreationForm):
    twitch_url = forms.URLField(label="Ссылка на Twitch", max_length=200)
    photo = forms.ImageField(label="Фотография", required=False)
    namestreamer = forms.CharField(label="Имя стримера", max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
