from django import forms
from shop.models import AddProduct


class AddproductForms(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ["nameproduct", "photoproduct", "price"]


class DeleteProductforms(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = ()
