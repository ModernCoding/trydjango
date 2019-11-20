from django import forms

from .models import Article

class BlogForm(forms.ModelForm):
  
  title         = forms.CharField(
      widget=forms.TextInput(attrs={
          "placeholder": "Your title"
        })
    )
  
  content       = forms.CharField(
      widget=forms.Textarea(attrs={
          "placeholder": "Your content",
          "rows": 19,
          "cols": 40
        })
    )

  
  class Meta:

    model = Article

    fields = [
      'title',
      'content: '
    ]


  def clean_title(self, *args, **kwargs):

    title = self.cleaned_data.get('title')

    if not "CFE" in title:
      raise forms.ValidationError("This is not a valid title")
    
    if not "news" in title:
      raise forms.ValidationError("This is not a valid title")

    return title