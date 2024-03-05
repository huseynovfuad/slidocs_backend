from rest_framework import generics
from .models import About, PrivacyPolicy, TermCondition, RefundPolicy, Contact
from .serializers import (
    AboutSerializer, TermConditionSerializer,
    RefundPolicySerializer, PrivacyPolicySerializer, ContactSerializer
)


class AboutView(generics.RetrieveAPIView):
    serializer_class = AboutSerializer
    permission_classes = ()

    def get_object(self):
        return About.objects.last()


class PrivacyPolicyView(generics.RetrieveAPIView):
    serializer_class = PrivacyPolicySerializer
    permission_classes = ()

    def get_object(self):
        return PrivacyPolicy.objects.last()


class TermConditionView(generics.RetrieveAPIView):
    serializer_class = TermConditionSerializer
    permission_classes = ()

    def get_object(self):
        return TermCondition.objects.last()


class RefundPolicyView(generics.RetrieveAPIView):
    serializer_class = RefundPolicySerializer
    permission_classes = ()

    def get_object(self):
        return RefundPolicy.objects.last()



class ContactView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    permission_classes = ()