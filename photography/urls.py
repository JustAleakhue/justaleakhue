from django.urls import path
from . import views


app_name = 'photography'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('Gallery/', views.Gallery, name='gallery'),
    path('Photogallery/', views.Photogallery, name='Photogallery'),
]