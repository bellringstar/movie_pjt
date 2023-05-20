from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    self_introduction = serializers.CharField()
    profile_image = serializers.ImageField(use_url=True)

