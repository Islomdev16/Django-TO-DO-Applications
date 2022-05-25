from django.db import models

# Create your models here.
class Mytodo(models.Model):
    tasks = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
