from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View

from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

from .models import Course
from .forms import CourseModelForm


# Base view class = View

class CourseView(View):
  
  template_name = 'courses/course_list.html'
  queryset = Course.objects.all()

  def get_queryset(self):
    return self.queryset


  def get(self, request, id=None, *args, **kwargs):
    # return render(request, 'about.html', {})

    context = {}

    if id is None:
      context['object_list'] = self.get_queryset()

    else:
      obj = get_object_or_404(Course, id=self.kwargs.get("id"))
      self.template_name = 'courses/course_detail.html'
      context['object'] = obj
  

    return render(request, self.template_name, context)


class MyCourseListView(CourseView):
  queryset = Course.objects.filter(id=1)


class CourseCreateView(View):
  
  template_name = 'courses/course_create.html'

  def get(self, request, *args, **kwargs):
    
    return render(
        request,
        self.template_name,
        { "form": CourseModelForm() }
      )


  def post(self, request, *args, **kwargs):

    form = CourseModelForm(request.POST)

    if form.is_valid():
      form.save()

    return render(request, self.template_name, { "form": form })


class CourseUpdateView(View):
  
  template_name = 'courses/course_create.html'

  def get_object(self):

    id = self.kwargs.get("id")

    if id is None:
      return None

    else:
      return get_object_or_404(Course, id=id)


  def get(self, request, id=None, *args, **kwargs):

    context = {}
    obj = self.get_object()

    if obj is not None:
      form = CourseModelForm(instance=obj)
      context['object'] = obj
      context['form'] = form

    return render(request, self.template_name, context)


  def post(self, request, id=None, *args, **kwargs):

    context = {}
    obj = self.get_object()

    if obj is not None:
      form = CourseModelForm(request.POST, instance=obj)
      context['object'] = obj
      context['form'] = form

    if form.is_valid():
      form.save()
    

    return render(request, self.template_name, context)


class CourseDeleteView(View):
  
  template_name = 'courses/course_delete.html'

  def get_object(self):

    id = self.kwargs.get("id")

    if id is None:
      return None

    else:
      return get_object_or_404(Course, id=id)


  def get(self, request, id=None, *args, **kwargs):

    context = {}
    obj = self.get_object()

    if obj is not None:
      context['object'] = obj

    return render(request, self.template_name, context)


  def post(self, request, id=None, *args, **kwargs):

    context = {}
    obj = self.get_object()

    if obj is not None:
      obj.delete()
      context['object'] = None
      return redirect('/courses/')

    return render(request, self.template_name, context)


# HTTP METHODS

def my_fbv(request, *args, **kwargs):
  return render(request, 'about.html', {})