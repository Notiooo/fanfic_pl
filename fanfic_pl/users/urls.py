from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path('<int:pk>/', views.CustomProfileView.as_view(), name="profile")
]