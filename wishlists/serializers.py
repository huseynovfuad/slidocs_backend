from rest_framework import serializers
from templates.serializers import TemplateSerializer
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ("id", "user", "template")
        extra_kwargs = {
            "user": {"read_only": True},
        }


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        repr_["template"] = TemplateSerializer(instance.template).data
        repr_["success"] = True
        return repr_ if instance.id else {"success": False}


    def create(self, validated_data):
        wishlist, created = Wishlist.objects.get_or_create(
            **validated_data
        )
        return wishlist