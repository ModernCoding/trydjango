from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
  CreateView,
  DetailView,
  ListView,
  UpdateView,
  DeleteView
)

from .models import Course
from .forms import CourseModelForm


# Create your views here.

class CourseListView(ListView):
  queryset = Course.objects.all()


class CourseDetailView(DetailView):

  def get_object(self):
    return get_object_or_404(Course, id=self.kwargs.get("id"))


class CourseCreateView(CreateView):
  
  template_name = 'courses/course_create.html'
  form_class = CourseModelForm
  queryset = Course.objects.all()

  def form_valid(self, form):
    print(form.cleaned_data)
    return super().form_valid(form)

  def get_success_url(self):
    return reverse('courses:course-list')


class CourseUpdateView(UpdateView):
  
  template_name = 'courses/course_create.html'
  form_class = CourseModelForm

  def form_valid(self, form):
    return super().form_valid(form)

  def get_object(self):
    return get_object_or_404(Course, id=self.kwargs.get("id"))


class CourseDeleteView(DeleteView):
  
  template_name = 'courses/course_delete.html'

  def get_object(self):
    return get_object_or_404(Course, id=self.kwargs.get("id"))

  def get_success_url(self):
    return reverse('courses:course-list')