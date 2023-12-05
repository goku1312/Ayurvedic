from django.urls import path
from app import views
urlpatterns = [
    
    path("",views.home),
    path("home",views.home),
    path("about",views.about),
     path("product",views.product),
    path("feature",views.feature),
    path("howtouse",views.howtouse),
        path("testimonial",views.testimonial),
     path("blog",views.blog),
    path("404",views.e404),
    path("contact",views.contact),
]
