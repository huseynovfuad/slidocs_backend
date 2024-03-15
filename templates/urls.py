from django.urls import path
from . import views

app_name = "templates"

urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="categories"),
    path("platforms/", views.PlatformListView.as_view(), name="platforms"),
    path("list/", views.TemplateListView.as_view(), name="list"),
    path("template-info/<id>/", views.TemplateDetailView.as_view(), name="detail")
]