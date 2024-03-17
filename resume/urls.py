from django.contrib import admin
from django.urls import path ,include
from . views import IndexView ,ContactView

urlpatterns = [
    path('', IndexView.as_view()),
    path('contact/', ContactView.as_view()),

]