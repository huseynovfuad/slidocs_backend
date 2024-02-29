from django.urls import path
from . import views

app_name = "wishlist"

urlpatterns = [
    path("list/", views.WishlistListView.as_view(), name="list"),
    path("add/", views.WishlistCreateView.as_view(), name="add"),
    path("delete/<id>/", views.WishlistDeleteView.as_view(), name="delete"),
]