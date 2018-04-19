# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
year_str = "20%02d-%02d"
YEAR_CHOICES = [(year_str %(x,x+1), year_str %(x,x+1)) for x in range(6,18)]
SEM_CHOICES = [(x,x) for x in range(1,4)]

class department(models.Model):
    code = models.CharField(max_length = 5, primary_key = True)
    name = models.CharField(max_length = 20, blank = True)

    def __unicode__(self):
        return self.code

class course(models.Model):
    code = models.CharField(max_length=8, primary_key=True)
    title = models.CharField(max_length=50)
    dept = models.ForeignKey(department)
    desc = models.TextField()

    def __unicode__(self):
        return self.code

class student(models.Model):
    rollno = models.CharField(max_length=8, primary_key = True)
    dept = models.ForeignKey(department, blank = True, default = None)
    name = models.CharField(max_length = 20)
    program = models.CharField(max_length = 10)

class enrolled(models.Model):
    rollno = models.ForeignKey(student)
    ccode = models.ForeignKey(course)
    instructor = models.CharField(max_length = 20)
    acad_year = models.CharField(max_length = 10)
    semester = models.IntegerField()
    
    class Meta:
        unique_together = (('rollno','acad_year','semester','ccode'),)

