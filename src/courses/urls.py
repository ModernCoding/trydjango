from django.urls import path

from .views import (
    # my_fbv,
    CourseView,
    CourseCreateView,
    CourseDetailView,
    CourseListView,
    CourseUpdateView,
    CourseDeleteView
  )


app_name = 'courses'

urlpatterns = [
  # path('', my_fbv, name='courses-list'),
  path(
    '',
    CourseView.as_view(template_name='contact.html'),
    name='courses-list'
  ),
  
  # path('', CourseListView.as_view(), name='course-list'),
  
  path(
    # '<int:pk>/',
    '<int:id>/',
    CourseDetailView.as_view(),
    name='course-detail'
  ),
  
  path(
    'create/',
    CourseCreateView.as_view(),
    name='course-create'
  ),
  
  path(
    '<int:id>/update',
    CourseUpdateView.as_view(),
    name='course-update'
  ),
  
  path(
    '<int:id>/delete',
    CourseDeleteView.as_view(),
    name='course-delete'
  )
]
