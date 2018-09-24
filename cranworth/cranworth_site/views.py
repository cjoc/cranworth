"""
VIEWS
Defines views to be used in this application.
Cameron O'Connor, 2018
"""

from .models import *
from django.shortcuts import render, get_object_or_404


# Category View
# Shows all firms which pertain to the given category.

def category_view(request, category_id):
    category = get_object_or_404(Category, category_id=category_id)
    firms = Firm.objects.filter(category=category)
    return render(request, 'cranworth_site/category-view.html', {'firms': firms})


# Firm View
# Shows details of given firm.

def firm_view(request, firm_id):
    firm = get_object_or_404(Firm, firm_id=firm_id)
    student = Student.objects.get(user_id=request.user.username)
    reviews = Review.objects.filter(firm=firm)
    return render(request, 'cranworth_site/firm-view.html', {'firm': firm,
                                                             'student': student,
                                                             'reviews': reviews})

# Landing
# Shows landing page, inviting user to authenticate.

def landing(request):
    return render(request, 'cranworth_site/landing.html')