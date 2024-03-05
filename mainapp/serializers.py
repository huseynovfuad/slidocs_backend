from rest_framework import serializers
from .models import About, PrivacyPolicy, TermCondition, RefundPolicy, Contact


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model  = About
        fields = "__all__"


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = "__all__"



class TermConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermCondition
        fields = "__all__"


class RefundPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = RefundPolicy
        fields = "__all__"



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"