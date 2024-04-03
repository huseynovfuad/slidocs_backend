from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import (
    LoginSerializer, RegisterSerializer,
    ActivationSerializer, ChangePasswordSerializer,
    ProfileSerializer
)

User = get_user_model()


class LoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = ()



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = ()


class ActivationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ActivationSerializer
    lookup_field = "code"
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(data=request.data, context={"user": user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)



class ChangePasswordView(generics.CreateAPIView):
    serializer_class = ChangePasswordSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)



class ProfileView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user
