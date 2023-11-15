from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework import validators

from user_app.models import Customer


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=(validators.UniqueValidator(queryset=User.objects.all()),)
    )
    email = serializers.CharField(
        required=True,
        validators=(validators.UniqueValidator(queryset=User.objects.all()),)
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        validators=(validate_password,)
    )
    confirm_password = serializers.CharField(
        required=True,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'confirm_password')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError(
                {'password': "Password fields didn't match"}
            )
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=(validate_password,))
    confirm_password = serializers.CharField(required=True)


class CustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Customer
        fields = ["id", "username", "followers", "is_verified"]
