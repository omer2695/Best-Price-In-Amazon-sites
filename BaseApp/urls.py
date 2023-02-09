from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomePage, name='HomePage'),
    path('SearchPage/', views.SearchPage, name='SearchPage'),
    path('Compare_Page/', views.Compare_Page, name='Compare_Page'),
]