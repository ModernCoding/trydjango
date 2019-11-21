from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):

  title = models.CharField(max_length=120)
  description = models.TextField()
  price = models.DecimalField(max_digits=1000, decimal_places=2)


  def get_absolute_url(self):
    return reverse("courses:course-detail", kwargs={ "id": self.id })