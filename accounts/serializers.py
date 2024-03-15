import re
import string
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .utils import EmailThread
from .generators import create_code_shortcode

User = get_user_model()


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "name", "surname", "password")
        extra_kwargs = {
            "name": {"read_only": True},
            "surname": {"read_only": True},
        }


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if User.objects.filter(email=email, is_active=False).exists():
            raise serializers.ValidationError({"error": "This account is not activated"})

        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError({"error": "Email or password is wrong"})

        return attrs


    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        return authenticate(email=email, password=password)


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return repr_



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "name", "surname", "code", "password", "password_confirm")
        extra_kwargs = {
            "code": {"read_only": True}
        }


    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password").strip()
        password_confirm = attrs.get("password_confirm").strip()

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "Email with this email already exists"})

        if len(password) < 8:
            raise serializers.ValidationError({"error": "Password must be at least 8 characters long."})

        if not re.search(r'[A-Z]', password):
            raise serializers.ValidationError({"error": "Password must contain at least one uppercase letter."})

        if not re.search(r'[a-z]', password):
            raise serializers.ValidationError({"error": "Password must contain at least one lowercase letter."})

        if not re.search(r'[0-9]', password):
            raise serializers.ValidationError({"error": "Password must contain at least one digit."})

        if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', password):
            raise serializers.ValidationError({"error": "Password must contain at least one special character."})

        if password != password_confirm:
            raise serializers.ValidationError({"error": "Passwords should match"})

        return attrs


    def create(self, validated_data):
        validated_data.pop("password_confirm")
        password = validated_data.pop("password")
        user = User(
            **validated_data, is_active=False,
            activation_code=create_code_shortcode(size=6, model_=User, elements=string.digits)
        )
        user.set_password(password)
        user.save()

        EmailThread(
            subject="Activation email | Slidocs",
            html_content=f"Your activation code: {user.activation_code}",
            recipient_list=[user.email]
        ).run()
        return user



class ActivationSerializer(serializers.ModelSerializer):
    activation_code = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "name", "surname", "activation_code", )
        extra_kwargs = {
            "email": {"read_only": True},
            "name": {"read_only": True},
            "surname": {"read_only": True},
        }


    def validate(self, attrs):
        user = self.context.get("user")
        activation_code = attrs.get("activation_code")

        if user.activation_code != activation_code:
            raise serializers.ValidationError({"error": "Wrong credentials"})

        return attrs


    def create(self, validated_data):
        user = self.context.get("user")
        user.is_active = True
        user.activation_code = None
        user.save()
        return user


    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return repr_



class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    new_password_confirm = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = User
        fields = (
            "email", "code", "name", "surname",
            "old_password", "new_password", "new_password_confirm"
        )
        extra_kwargs = {
            "email": {"read_only": True},
            "code": {"read_only": True},
            "name": {"read_only": True},
            "surname": {"read_only": True},
            "old_password": {"write_only": True},
            "new_password": {"write_only": True},
            "new_password_confirm": {"write_only": True},
        }

    def validate(self, attrs):
        user = self.context.get("user")
        old_password = attrs.get("old_password")
        new_password = attrs.get("new_password")
        new_password_confirm = attrs.get("new_password_confirm")

        if not user.check_password(old_password):
            raise serializers.ValidationError({"error": "Wrong password"})

        if len(new_password) < 8:
            raise serializers.ValidationError({"error": "Password must be at least 8 characters long."})

        if not re.search(r'[A-Z]', new_password):
            raise serializers.ValidationError({"error": "Password must contain at least one uppercase letter."})

        if not re.search(r'[a-z]', new_password):
            raise serializers.ValidationError({"error": "Password must contain at least one lowercase letter."})

        if not re.search(r'[0-9]', new_password):
            raise serializers.ValidationError({"error": "Password must contain at least one digit."})

        if not re.search(r'[!@#$%^&*()\-_=+{};:,<.>]', new_password):
            raise serializers.ValidationError({"error": "Password must contain at least one special character."})

        if new_password_confirm != new_password_confirm:
            raise serializers.ValidationError({"error": "Passwords must match"})

        return attrs


    def create(self, validated_data):
        user = self.context.get("user")
        new_password = validated_data.pop("new_password")
        user.set_password(new_password)
        user.save()
        return user

    def to_representation(self, instance):
        repr_ = super().to_representation(instance)
        token = RefreshToken.for_user(instance)
        repr_["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return repr_