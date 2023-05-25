from django import forms
from shop.models import AddProduct
from lkusers.models import ContribUsers


class AddproductForms(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ["nameproduct", "photoproduct", "price"]


class addPhoto_Telega(forms.ModelForm):
    class Meta:
        model = ContribUsers
        fields = {"photouser","telegramm"}


class DeleteProductforms(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ()

