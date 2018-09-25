"""cranworth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import cranworth_site.views as views

app_name = 'cranworth_site'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.home, name='home'),
    path('firm/<int:firm_id>', views.firm_view, name='firm-view'),
    path('category/<int:category_id>', views.category_view, name='category-view'),
    path('firms', views.firms_list, name='firms-list'),
    path('magic-circle', views.magic_circle_list, name='magic-circle'),
    path('honorable-mentions', views.honorable_mentions_list, name='honorable-mentions'),
    path('about', views.about, name='about'),
    path('landing', views.landing, name='landing'),
    path(r'', include('ucamwebauth.urls')),
    path(r'', include('tinymce.urls')),
]
