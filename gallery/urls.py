from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('Gallery/', views.Gallery, name='gallery'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('gallery/<int:pk>/', views.detail, name='gallery-detail'),
    path('photo/<int:pk>/', views.photo_detail, name='photo-detail'),
]