"""
VIEWS
Defines views to be used in this application.
Cameron O'Connor, 2018
"""

from .models import *
from django.shortcuts import render, get_object_or_404
from random import randint


# Category View
# Shows all firms which pertain to the given category.

def category_view(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)
    categories = Category.objects.order_by('name')
    student = Student.objects.get(user_id=request.user.username)
    firms = Firm.objects.filter(category=category).order_by('name')
    return render(request, 'cranworth_site/category-view.html', {'firms': firms,
                                                                 'student': student,
                                                                 'category': category,
                                                                 'categories': categories})


# Firm View
# Shows details of given firm.

def firm_view(request, firm_id):
    firm = get_object_or_404(Firm, firm_id=firm_id)
    student = Student.objects.get(user_id=request.user.username)
    reviews = Review.objects.filter(firm=firm)
    return render(request, 'cranworth_site/firm-view.html', {'firm': firm,
                                                             'student': student,
                                                             'reviews': reviews})

def firms_list(request):
    student = Student.objects.get(user_id=request.user.username)
    firms = Firm.objects.order_by('name')
    categories = Category.objects.order_by('name')
    return render(request, 'cranworth_site/firms-list.html', {'firms': firms,
                                                              'student': student,
                                                              'categories': categories})

# Landing
# Shows landing page, inviting user to authenticate.

def landing(request):
    return render(request, 'cranworth_site/landing.html')


# About
# Shows page with some information about this site.

def about(request):
    student = Student.objects.get(user_id=request.user.username)
    return render(request, 'cranworth_site/about.html', {'student': student})


# Home
# Shows homepage with welcome message & quick links.

def home(request):
    student = Student.objects.get(user_id=request.user.username)
    honorable_mentions = Firm.objects.filter(honorable_mention=True)
    count = honorable_mentions.count()
    if count == 0:
        honorable_mention = None
    else:
        r = randint(0, count-1)
        honorable_mention = honorable_mentions[r]
    magic_circles = Firm.objects.filter(magic_circle=True)
    count = magic_circles.count()
    if count == 0:
        magic_circle = None
    else:
        r = randint(0, count - 1)
        magic_circle = magic_circles[r]
    return render(request, 'cranworth_site/home.html', {'student': student,
                                                        'honorable_mention': honorable_mention,
                                                        'magic_circle': magic_circle})