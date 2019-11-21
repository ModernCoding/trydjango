# from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm


# Create your views here.

def product_list_view(request):
  
  # queryset = Product.objects.all()
  
  return render(
      request,
      "products/product_list.html",
      { "object_list": Product.objects.all() }
    )


def product_detail_view(request, id):

  # try:
  #   obj = Product.objects.get(id=id)

  # except Product.DoesNotExist:
  #   # raise Http404
  #   return HttpResponse("<h1>DTC</h1>")
  

  # context = {
  #   "title": obj.title,
  #   "description": obj.description,
  # }
  
  return render(
      request,
      "products/product_detail.html",
      # { "object": obj } # context
      { "object": get_object_or_404(Product, id=id) }
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


def product_update_view(request, id):

  obj = get_object_or_404(Product, id=id)

  form = ProductForm(
      request.POST or None,
      initial=initial_data,
      instance=obj
    )

  if form.is_valid():
    form.save()

  return render(
      request,
      "products/product_create.html",
      { "form": form }
    )
  

def product_delete_view(request, id):

  obj = get_object_or_404(Product, id=id)

  if request.method == "POST":
    obj.delete()
    return redirect('../../')

  
  return render(
      request,
      "products/product_delete.html",
      { "object": obj } # context
    )