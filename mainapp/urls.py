from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("term-conditions/", views.TermConditionView.as_view(), name="term-conditions"),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path("refund-policy/", views.RefundPolicyView.as_view(), name="refund-policy"),
]