from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  
  class Meta:
    model = Product

    fields = [
      'title',
      'description',
      'price'
    ]


class RawProductForm(forms.Form):
  title         = forms.CharField(
      label="Product name",
      widget=forms.TextInput(attrs={
          "placeholder": "Your title"
        })
    )
  
  description   = forms.CharField(
      required=False,
      widget=forms.Textarea(attrs={
          "placeholder": "Your description",
          "class": "new-class-name two",
          "id": "my-id-for-textarea",
          "rows": 19,
          "cols": 40
        })
    )
  
  price         = forms.DecimalField(initial=4.19)
