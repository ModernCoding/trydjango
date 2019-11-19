from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
  
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

  
  class Meta:

    model = Product

    fields = [
      'title',
      'description',
      'price'
    ]


  def clean_title(self, *args, **kwargs):

    title = self.cleaned_data.get('title')

    if not "CFE" in title:
      raise forms.ValidationError("This is not a valid title")
    
    if not "news" in title:
      raise forms.ValidationError("This is not a valid title")

    return title


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
