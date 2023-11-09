from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.TextField(max_length=128)
    isbn = models.TextField(max_length=24)
