from django import forms
from lkusers.models import UserBuy, HisStreamers


class BuyproductForms(forms.ModelForm):
    class Meta:
        model = UserBuy
        fields = []


class BalanceCheckForms(forms.ModelForm):
    class Meta:
        model = HisStreamers
        fields = ()
