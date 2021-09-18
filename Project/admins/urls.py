from django.urls import path
from . import views

urlpatterns = [
    path('',views.main, name = 'main_url'),
    
    path('user_detail/',views.user_detail, name = 'user_detail_url'),
    path('add_user/', views.add_user, name="add_user_url"),
    path('edit_user/<int:id>/', views.edit_user, name="edit_user_url"),
    path('delete_user/<int:id>/',views.delete_user, name = 'delete_user_url'),
    
    path('contact_detail/',views.contact_detail, name = 'contact_detail_url'),
    path('add_contact/', views.add_contact, name="add_contact_url"),
    path('edit_contact/<int:id>/', views.edit_contact, name="edit_contact_url"),
    path('delete_contact/<int:id>/',views.delete_contact, name = 'delete_contact_url'),
    
    path('amazon_deals/',views.amazon_deals, name = 'amazon_deals_url'),
    path('add_amazon/', views.add_amazon, name="add_amazon_url"),
    path('edit_amazon/<int:id>/', views.edit_amazon, name="edit_amazon_url"),
    path('delete_amazon/<int:id>/',views.delete_amazon, name = 'delete_amazon_url'),
    
    path('flipkart_deals/',views.flipkart_deals, name = 'flipkart_deals_url'),
    path('add_flipkart/', views.add_flipkart, name="add_flipkart_url"),
    path('edit_flipkart/<int:id>/', views.edit_flipkart, name="edit_flipkart_url"),
    path('delete_flipkart/<int:id>/',views.delete_flipkart, name = 'delete_flipkart_url'),
    
    path('snapdeal_deals/',views.snapdeal_deals, name = 'snapdeal_deals_url'),
    path('add_snapdeal/', views.add_snapdeal, name="add_snapdeal_url"),
    path('edit_snapdeal/<int:id>/', views.edit_snapdeal, name="edit_snapdeal_url"),
    path('delete_snapdeal/<int:id>/',views.delete_snapdeal, name = 'delete_snapdeal_url'),
    
    
    
    
]