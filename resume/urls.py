from django.contrib import admin
from django.urls import path ,include
from . views import IndexView ,ContactView,BlogView,PortfolioView ,BlogDetailView,PortfolioDetailView

urlpatterns = [
    path('', IndexView.as_view()),
    path('contact/', ContactView.as_view()),
    path('blog/', BlogView.as_view()),
    path('portfolio/', PortfolioView.as_view()),
    path('blog/<slug:slug>', BlogDetailView.as_view()),
    path('portfolio/<slug:slug>', PortfolioDetailView.as_view()),

]