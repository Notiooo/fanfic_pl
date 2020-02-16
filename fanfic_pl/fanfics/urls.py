from django.urls import path
from . import views

urlpatterns = [
    path('', views.FandomsHomeView.as_view(), name='fandoms'),

    path('<slug:slug_fandom>/add_fanfic/', views.AddFanfic.as_view(), name='add_fanfic'),
    path('<slug:slug_fandom>/', views.FandomView.as_view(), name='fandom'),
]