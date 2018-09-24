from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Firm)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Review)
admin.site.register(Area)

admin.site.site_header = "Cranworth Law Society"
admin.site.site_title = "Cranworth Law Society"
admin.site.index_title = "Backend Administration"