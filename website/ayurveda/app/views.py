from django.shortcuts import render,HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def product(request):
    return render(request,"product.html")

def feature(request):
    return render(request,"feature.html")

def howtouse(request):
    return render(request,"how-to-use.html")

def testimonial(request):
    return render(request,"testimonial.html")

def blog(request):
    return render(request,"blog.html")

def e404(request):
    return render(request,"404.html")

def contact(request):
    return render(request,"contact.html")
