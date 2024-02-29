from rest_framework import serializers
from .models import Basket
from templates.serializers import TemplateSerializer


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ("id", "user", "template", "quantity")
        extra_kwargs = {
            "user": {"read_only": True},
            "quantity": {"read_only": True},
        }


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["template"] = TemplateSerializer(instance.template).data
        return repr_


    def create(self, validated_data):
        basket, created = Basket.objects.get_or_create(
            **validated_data
        )
        if not created:
            basket.quantity += 1
            basket.save()
        return basket


    def update(self, instance, validated_data):
        if instance.quantity == 1:
            return instance

        instance.quantity -= 1
        instance.save()
        return instance