from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("activate/<code>/", views.ActivationView.as_view(), name="activation"),
    path("change-password/", views.ChangePasswordView.as_view(), name="change-password"),
    path("profile/", views.ProfileView.as_view(), name="profile")
]
