from django.urls import path
from . import views


app_name = 'conversation'

urlpatterns = [
    path('new/<int:gallery_pk>/', views.new_conversation, name='new'),
]