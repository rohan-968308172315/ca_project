from django.urls import path,include
from core import views

urlpatterns = [
    path('',views.index),
    path('about_us/',views.about_us),
    path('faqs/',views.faqs),
    path('teams/',views.teams),
    path('gallery/',views.gallery),
    path('testimonial/',views.testimonial),
    path('contact/',views.contact),
]