from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name= "home"),
    path('abouts', views.abouts , name= "abouts"),
    path('contact', views.contact , name= "contact"),
    path('services', views.services , name= "services")
]
