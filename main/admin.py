# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(course)
admin.site.register(department)
admin.site.register(student)
admin.site.register(enrolled)
