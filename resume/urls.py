from django.contrib import admin
from django.urls import path ,include
from . views import IndexView ,ContactView,BlogView,PortfolioView

urlpatterns = [
    path('', IndexView.as_view()),
    path('contact/', ContactView.as_view()),
    path('blog/', BlogView.as_view()),
    path('portfolio/', PortfolioView.as_view()),

]