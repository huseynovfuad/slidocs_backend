from rest_framework import generics
from .serializers import (
    CategorySerializer, PlatformSerializer, TemplateSerializer
)
from .models import (
    Category, Platform, Template
)
from .paginations import CustomPagination


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.order_by("name")
    serializer_class = CategorySerializer
    permission_classes = ()



class PlatformListView(generics.ListAPIView):
    queryset = Platform.objects.order_by("name")
    serializer_class = PlatformSerializer
    permission_classes = ()


class TemplateListView(generics.ListAPIView):
    queryset = Template.objects.order_by("-id")
    serializer_class = TemplateSerializer
    permission_classes = ()
    pagination_class = CustomPagination



class TemplateDetailView(generics.RetrieveAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = ()
    lookup_field = "id"