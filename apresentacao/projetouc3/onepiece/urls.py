from django.contrib import admin
from django.urls import path

from.import views

urlpatterns = [
    path('', views.onepiece, name = 'onepiece'),
    # path('home/', views.home)
]