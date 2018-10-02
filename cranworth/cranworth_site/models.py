"""
MODELS
Defines database models to be used in this application.
Cameron O'Connor, 2018
"""

from django.db import models


# Category of law firm, e.g. 'commercial'.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Law firm.

class Firm(models.Model):
    firm_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100)
    is_chamber = models.BooleanField('Is Chamber?', default=False)
    logo = models.ImageField('Logo', upload_to='firm_logos', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=None)
    description = models.TextField('Summary', blank=True, null=True)
    areas = models.TextField('Areas', blank=True, null=True)
    cranworth_links = models.TextField('Cranworth Links', blank=True, null=True)
    opportunities_deadlines = models.TextField('Opportunities & Deadlines', blank=True, null=True)
    excerpt = models.TextField('Excerpt', blank=True, null=True)
    address = models.CharField('Address', max_length=100, blank=True, null=True)
    contact_name = models.CharField('Contact Name', max_length=100, blank=True, null=True)
    contact_email = models.EmailField('Contact Email', blank=True, null=True)
    website = models.URLField('Website URL', blank=True, null=True)
    magic_circle = models.BooleanField('Is Magic Circle?')
    honorable_mention = models.BooleanField('Is Honorable Mention?')

    def __str__(self):
        return self.name


# Student member of Cranworth who can access the website.

class Student(models.Model):
    user_id = models.CharField('CRSid', max_length=10)
    first_name = models.CharField('First Name', max_length=50)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.surname


# Review of a law firm which a student has left.

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    author = models.CharField('Author Name', max_length=100)
    firm = models.ForeignKey(Firm, on_delete=models.SET_DEFAULT, default=None)
    title = models.CharField('Title', max_length=500)
    description = models.TextField('Review Text')

    def __str__(self):
        return "Review " + str(self.review_id) + " - " + str(self.firm)


# Static page.

class StaticPage(models.Model):
    page_id = models.AutoField(primary_key=True)
    title = models.CharField('Title', max_length=150)
    text = models.TextField('Body Text', blank=True, null=True)

    def __str__(self):
        return self.title