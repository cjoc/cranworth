"""
VIEWS
Defines views to be used in this application.
Cameron O'Connor, 2018
"""

from .models import *
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from random import randint


# Category View
# Shows all firms which pertain to the given category.

def category_view(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)
    static_pages = StaticPage.objects.all()
    categories = Category.objects.order_by('name')
    student = Student.objects.get(user_id=request.user.username)
    firms = Firm.objects.filter(category=category).order_by('name')
    return render(request, 'cranworth_site/category-view.html', {'firms': firms,
                                                                 'student': student,
                                                                 'category': category,
                                                                 'categories': categories,
                                                                 'static_pages': static_pages})


# Firm View
# Shows details of given firm.

def firm_view(request, firm_id):
    firm = get_object_or_404(Firm, firm_id=firm_id)
    student = Student.objects.get(user_id=request.user.username)
    reviews = Review.objects.filter(firm=firm)
    return render(request, 'cranworth_site/firm-view.html', {'firm': firm,
                                                             'student': student,
                                                             'reviews': reviews})


# Firms List
# Lists all firms, irrespective of category.

def firms_list(request):
    student = Student.objects.get(user_id=request.user.username)
    static_pages = StaticPage.objects.all()
    firms = Firm.objects.order_by('name')
    categories = Category.objects.order_by('name')
    return render(request, 'cranworth_site/firms-list.html', {'firms': firms,
                                                              'student': student,
                                                              'categories': categories,
                                                              'static_pages': static_pages})


# Magic Circle List
# Lists all firms which are in the magic circle.

def magic_circle_list(request):
    student = Student.objects.get(user_id=request.user.username)
    static_pages = StaticPage.objects.all()
    firms = Firm.objects.filter(magic_circle=True).order_by('name')
    categories = Category.objects.order_by('name')
    return render(request, 'cranworth_site/magic-circle-list.html', {'firms': firms,
                                                                     'student': student,
                                                                     'categories': categories,
                                                                     'static_pages': static_pages})


# Landing
# Shows landing page, inviting user to authenticate.

def landing(request):
    return render(request, 'cranworth_site/landing.html')


# About
# Shows page with some information about this site.

def about(request):
    student = Student.objects.get(user_id=request.user.username)
    static_pages = StaticPage.objects.all()
    categories = Category.objects.order_by('name')
    return render(request, 'cranworth_site/about.html', {'student': student,
                                                         'categories': categories,
                                                         'static_pages': static_pages})


# Error
# Shows error message explaining user is not a society member.

def error(request):
    return render(request, 'cranworth_site/error.html')


# Home
# Shows homepage with welcome message & quick links.

def home(request):
    student = Student.objects.get(user_id=request.user.username)
    static_pages = StaticPage.objects.order_by('title')
    categories = Category.objects.order_by('name')
    magic_circles = Firm.objects.filter(magic_circle=True)
    count = magic_circles.count()
    if count == 0:
        magic_circle_1 = None
        magic_circle_2 = None
    else:
        r1 = randint(0, count-1)
        r2 = randint(0, count-1)
        if r1 == r2 and count >= 2:
            if r1 > 0:
                r1 -= 1
            elif r2 > 0:
                r2 -= 1
            else:
                r2 += 1
        magic_circle_1 = magic_circles[r1]
        magic_circle_2 = magic_circles[r2]
    return render(request, 'cranworth_site/home.html', {'student': student,
                                                        'magic_circle_1': magic_circle_1,
                                                        'magic_circle_2': magic_circle_2,
                                                        'categories': categories,
                                                        'static_pages': static_pages})


# Static Page
# Shows simple static page with title and text.

def static_page(request, page_id):
    page = get_object_or_404(StaticPage, page_id=page_id)
    student = Student.objects.get(user_id=request.user.username)
    static_pages = StaticPage.objects.all()
    categories = Category.objects.order_by('name')
    return render(request, 'cranworth_site/static-page.html', {'student': student,
                                                               'static_pages': static_pages,
                                                               'categories': categories,
                                                               'page': page})


# 404
# Custom 404 page.

def handler404(request, exception, template_name='404.html'):
    response = render(request, 'cranworth_site/404.html', {})
    response.status_code = 404
    return response