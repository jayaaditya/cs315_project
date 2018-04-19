# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from main.models import *

# Create your views here.

def search_res(request):
    page=1
    pagenos = []
    next_page = "#"
    previous_page = "#"
    page_bool = False
    cards = []
    query = None
    try:
        page = eval(request.GET['page'])
    except:
        pass
    try:
        query = request.GET['query']
        queryset1 = student.objects.filter(rollno__icontains = query)
        queryset2 = student.objects.filter(name__icontains = query)
        final_query = (queryset1 | queryset2).distinct().order_by('rollno')
        rows = Paginator(final_query, 8)
        row = rows.page(page)
        page_bool = True
        if row.has_next():
            next_page = "/search/?query=%s&page=%s" %(query, str(row.next_page_number()))
        if row.has_previous():
            previous_page = "/search/?query=%s&page=%s" %(query, str(row.previous_page_number()))
        pagenos = [x for x in range(page,min(page+3,row.end_index()+1))]
        print row.end_index()
        cards = row.object_list
    except:
        row = []
    context = {
            'row' : cards, 
            'page_bool':page_bool, 
            'pagenos':pagenos,
            'next': next_page,
            'previous': previous_page,
            'query': query
            }
    return render(request, 'index.html', context)

def profile(request):
    try:
        rollno = request.GET['rollno']
        student_obj = student.objects.get(rollno = rollno)
    except:
        return HttpResponseRedirect('http://localhost:8000')
    context = {'student': student_obj}
    enroll_list = enrolled.objects.filter( rollno = student_obj).order_by('acad_year','semester')
    name_l = student_obj.name.split(' ')
    first_name = name_l[0]
    try:
        last_name = " ".join(name_l[1:])
    except:
        last_name = ""
    context['first_name'] = first_name
    context['last_name'] = last_name
    context['enrolled'] = enroll_list 
    return render(request, 'profile.html', context)

def main(request):
    return render(request, 'main.html')
