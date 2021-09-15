from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('about/', views.about, name='about_url'),
    path('contact/', views.contact, name='contact_url'),
    path('services/', views.services, name='services_url'),
    path('search_results/', views.search_result, name='search_url'),
    

]