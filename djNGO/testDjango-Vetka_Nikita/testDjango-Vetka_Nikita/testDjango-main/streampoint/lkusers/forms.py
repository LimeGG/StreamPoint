from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import ContribUsers

class UserProfileForm(UserChangeForm):
    class Meta:
        model = ContribUsers
        #image = forms.ImageField
        fields = ('photouser',)