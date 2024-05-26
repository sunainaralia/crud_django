from .models import User,UserCopy
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_no",
            "city",
            "state",
            "registration",
        ]


class UserCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCopy
        fields = [
            "id",
            "user_name",
            "status",
            "email",
            "phone_no",
            "profile_img",
            "address",
            "date",
        ]
