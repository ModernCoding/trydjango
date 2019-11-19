from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.

def product_detail_view(request, id):
  # obj = Product.objects.get(id=1)
  
  # context = {
  #   "title": obj.title,
  #   "description": obj.description,
  # }
  
  return render(
      request,
      "products/product_detail.html",
      { "object": Product.objects.get(id=id) }
    )


# def product_create_view(request):

#   form = RawProductForm()
  
#   if request.method == "POST":
#     form = RawProductForm(request.POST)

#     if form.is_valid():
#       print(form.cleaned_data)
#       Product.objects.create(**form.cleaned_data)

#     # else:
#     #   print(form.errors)


#   return render(
#       request,
#       "products/product_create.html",
#       { "form": form }
#     )


# def product_create_view(request):
#   print(request.GET)
#   print(request.POST)

#   if request.method == "POST":
#     print(request.POST.get('title'))

#   return render(
#       request,
#       "products/product_create.html",
#       {}
#     )


def product_create_view(request):

  initial_data = {
    "title": "From zero to hero"
  }

  # obj = Product.objects.get(id=2)

  form = ProductForm(
      request.POST or None,
      initial=initial_data,
      # instance=obj
    )

  if form.is_valid():
    form.save()
    form = ProductForm()

  return render(
      request,
      "products/product_create.html",
      { "form": form }
    )