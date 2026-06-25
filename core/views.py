from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,"home/index.html")

def about_us(req):
    return render(req,"home/about_us.html") 

def faqs(req):
    return render(req,"home/faqs.html")

def teams(req):
    return render(req,"home/teams.html")

def gallery(req):
    return render(req,"home/gallery.html")

def service(req):
    return render(req,"services/service.html")

def testimonial(req):
    return render(req,"home/testimonial.html")

def contact(req):
    return render(req,"home/contact.html")