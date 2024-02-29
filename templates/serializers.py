from rest_framework import serializers
from .models import (
    Category, Template, TemplateFile, Platform
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"



class TemplateSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Template
        fields = "__all__"


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        platform_list = TemplateFile.objects.filter(template=instance).values_list("platform", flat=True)
        repr_["platforms"] = PlatformSerializer(
            Platform.objects.filter(id__in=platform_list), many=True
        ).data
        return repr_