from django.urls import path,include
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('faqs/', views.faqs, name='faqs'),
    path('teams/', views.teams, name='teams'),
    path('gallery/', views.gallery, name='gallery'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),

    
    
    
    
    
]