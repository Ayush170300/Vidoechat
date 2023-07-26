from django.urls import path

from .templates.chat import views

urlpatterns = [
    path('', views.index, name='index'),
]