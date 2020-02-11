from django.urls import path
from . import views

urlpatterns = [
    path('', views.FandomsView.as_view(), name='fandoms'),
]