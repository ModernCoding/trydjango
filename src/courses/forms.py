from django import forms

from .models import Course

class CourseModelForm(forms.ModelForm):
  
  title         = forms.CharField(
      widget=forms.TextInput(attrs={
          "placeholder": "Your title"
        })
    )
  
  description   = forms.CharField(
      widget=forms.Textarea(attrs={
          "placeholder": "Your description",
          "rows": 19,
          "cols": 40
        })
    )

  
  class Meta:

    model = Course

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