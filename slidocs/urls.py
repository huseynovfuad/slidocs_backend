from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("api/accounts/", include("accounts.urls")),
    path("api/templates/", include("templates.urls")),
    path("api/baskets/", include("baskets.urls")),
    path("api/wishlists/", include("wishlists.urls")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



""" SWAGGER TOOLS """
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


schema_view = get_schema_view(
    openapi.Info(
        title="Slidocs API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@admin.remote"),
        license=openapi.License(name="Slidocs License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns += [
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('docs<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]