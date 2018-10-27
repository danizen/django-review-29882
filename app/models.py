# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    pages = models.IntegerField()

    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    addtl_authors = models.ManyToManyField(Author, related_name='credits')




