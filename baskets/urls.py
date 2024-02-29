from django.urls import path
from . import views

app_name = "baskets"

urlpatterns = [
    path("list/", views.BasketListView.as_view(), name="list"),
    path("add/", views.BasketCreateView.as_view(), name="add"),
    path("delete/<id>/", views.BasketDeleteView.as_view(), name="delete"),
    path("decrease/<id>/", views.BasketDecreaseView.as_view(), name="decrease"),
]