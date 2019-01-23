# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quizquestion(models.Model):
    q_name = models.CharField(max_length=200)
    opt1 = models.CharField(max_length=100)
    opt2 = models.CharField(max_length=100)
    opt3 = models.CharField(max_length=100)
    opt4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    q_id = models.IntegerField()

    def __str__(self):
        return self.q_name

class Sample(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
