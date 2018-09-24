"""
MODELS
Defines database models to be used in this application.
Cameron O'Connor, 2018
"""

from django.db import models
from tinymce.models import HTMLField


# Category of law firm, e.g. 'commercial'.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=100)

    def __str__(self):
        return self.title


# Law firm.

class Firm(models.Model):
    firm_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100)
    logo = models.ImageField('Logo', upload_to='firm_logos', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    description = models.TextField('Summary', blank=True, null=True)
    areas = models.ManyToManyField(Area, blank=True)
    ideal_description = models.TextField('The Ideal Candidate')
    opportunities_deadlines = models.TextField('Opportunities & Deadlines')
    excerpt = models.TextField('Excerpt', blank=True, null=True)
    address = models.CharField('Address', max_length=100, blank=True, null=True)
    contact_name = models.CharField('Contact Name', max_length=100, blank=True, null=True)
    contact_email = models.EmailField('Contact Email', blank=True, null=True)
    website = models.URLField('Website URL', blank=True, null=True)
    magic_circle = models.BooleanField('Is Magic Circle?')
    honorable_mention = models.BooleanField('Is Honorable Mention?')

    def __str__(self):
        return self.name


class Student(models.Model):
    user_id = models.CharField('CRSid', max_length=10)
    first_name = models.CharField('First Name', max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.surname


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    author = models.CharField('Author Name', max_length=100)
    firm = models.ForeignKey(Firm, on_delete=models.SET_DEFAULT, default=None)
    title = models.CharField('Title', max_length=500)
    description = models.TextField('Review Text')

    def __str__(self):
        return "Review " + str(self.review_id) + " - " + str(self.firm)
