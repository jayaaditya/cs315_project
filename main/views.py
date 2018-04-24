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
        query = request.GET['query'].strip()
        queryset1 = student.objects.filter(rollno__icontains = query)
        queryset2 = student.objects.filter(name__icontains = query)
        final_query = (queryset1 | queryset2).distinct().order_by('rollno')
        rows = Paginator(final_query, 8)
        row = rows.page(page)
        pagenos = [x for x in range(max(1,page-1),min(page+2,rows.num_pages + 1))]
        page_bool = True
        next_page = "/search/?query=%s&page=%s" %(query, str(rows.num_pages))
        previous_page = "/search/?query=%s&page=1" %(query)
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

def course_search(request):
    page_bool = False
    page=1
    pagenos = []
    next_page = "#"
    previous_page = "#"
    try:
        page = int(request.GET['page'])
    except:
        pass
    try:
        query = request.GET['query'].strip()
        course_list_1 = course.objects.filter(code__icontains = query)
        course_list_2 = course.objects.filter(title__icontains = query)
        course_list = (course_list_1 | course_list_2).distinct().order_by('code')
        rows = Paginator(course_list, 50)
        row = rows.page(page)
        page_bool = True
        pagenos = [x for x in range(max(1,page-1),min(page+2,rows.num_pages + 1))]
        next_page = "/course_search/?query=%s&page=%s" %(query, str(rows.num_pages))
        previous_page = "/course_search/?query=%s&page=1" %(query)
        context = {
                'courses' : row.object_list, 
                'page_bool':page_bool, 
                'pagenos':pagenos,
                'next': next_page,
                'previous': previous_page,
                'query': query
                }
        return render(request, 'course_search.html', context)
    except:
        return HttpResponseRedirect("/")

def course_disp(request):
    page=1
    try:
        page = int(request.GET['page'])
    except:
        pass
    try:
        code = request.GET['code'].strip()
        course_obj = course.objects.get( code = code)
    except:
        return HttpResponseRedirect('/')
    enrolled_list = enrolled.objects.filter( ccode = course_obj).order_by('acad_year','semester','rollno_id')
    rows = Paginator(enrolled_list, 100)
    row = rows.page(page)
    pagenos = [x for x in range(max(1,page-1),min(page+2,rows.num_pages + 1))]
    next_page = "/course/?code=%s&page=%s" %(code, str(rows.num_pages))
    previous_page = "/course/?code=%s&page=1" %(code)
    context = {
            'course' : course_obj,
            'enrolled':row.object_list,
            'pagenos':pagenos,
            'next': next_page,
            'previous': previous_page,
            }
    return render(request,'course_profile.html', context)
def course_inter(request):
    page = 1
    pagenos = []
    next_page = "#"
    previous_page = "#"
    page_bool = False
    cards = []
    try:
        page = int(request.GET['page'])
    except:
        pass
    try:
        query = request.GET['query'].split(',')
        query = map(lambda x: x.strip(), query)
        print query
    except:
        return HttpResponseRedirect('/')
    code1 = query.pop(0)
    e = enrolled.objects.select_related('rollno').filter(
            ccode__in = course.objects.filter(code__icontains = code1)
            )
    set_of_stud = set(map(lambda x: x.rollno.rollno, e))
    for x in query:
        e = enrolled.objects.select_related('rollno').filter(
                ccode__in = course.objects.filter(code__icontains = x)
                )
        set_of_stud &= set(map(lambda x: x.rollno.rollno, e))
    final_query = student.objects.filter(rollno__in = list(set_of_stud)).order_by('rollno')
    try:
        query = request.GET['query']
        rows = Paginator(final_query, 8)
        row = rows.page(page)
        pagenos = [x for x in range(max(1,page-1),min(page+2,rows.num_pages + 1))]
        page_bool = True
        next_page = "/inter/?query=%s&page=%s" %(query, str(rows.num_pages))
        print rows.num_pages
        previous_page = "/inter/?query=%s&page=1" %(query)
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
    return render(request, 'inter.html', context)

def main(request):
    return render(request, 'main.html')
