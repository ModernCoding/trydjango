from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
  print(args, kwargs)
  print(request.user)
  # return HttpResponse("<h1>Hello World!</h1>")
  return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Contact page</h1>")
  return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
  # return HttpResponse("<h1>About us</h1>")
  my_context = {
    "my_text": "this is about me",
    "this_is_true": True,
    "my_number": 123,
    "my_list": [3, 33, 43, "Abc"],
    "my_html": "<h1>Hello World!</h1>"
  }
  
  return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
  # return HttpResponse("<h1>Social page</h1>")
  return render(request, "social.html", {})
