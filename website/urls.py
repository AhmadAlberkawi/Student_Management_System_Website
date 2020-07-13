"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from studierendenverwaltung.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student_list, name='student_list'),
    path('student/add/', student_details, name='add_student'),
    path('student/edit/<int:pk>/', student_details, name='edit_student'),
    path('student_delete/<int:pk>/', student_delete, name='delete_student'),

    path('lehrveranstaltung/', lehrverantaltung_list, name='lehrverantaltung_list'),
    path('lehrveranstaltung/add/', lehrveranstaltung_details, name='add_lehrveranstaltung'),
    path('lehrveranstaltung/edit/<int:pk>', lehrveranstaltung_details, name='edit_lehrveranstaltung'),
    path('lehrveranstaltung/delete/<int:pk>', lehrveranstaltung_delete, name='delete_lehrveranstaltung')
]
