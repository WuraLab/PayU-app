# Serializers converted to query's into JSON, XML or other content types.
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpRequest
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token
from .models import Profile

class UserRegistrationSerializers(serializers.ModelSerializer):
    # User registration  api data formatter.
    class Meta:  #pylint: disable=too-few-public-methods
        # Return default User options fields.
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }
    #pylint: disable=R0201
    def create(self, validated_data): #create User && Profile profile model.
        profile_data = validated_data
        user = User.objects.create_user(**profile_data)
        Token.objects.create(user=user)
        Profile.objects.create(user=user)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    # User Profile  api data formatter.
    user = UserRegistrationSerializers()
    token = obtain_auth_token
    class Meta:    #pylint: disable=too-few-public-methods
        # Return Profile fields.
        model = Profile
        fields = ('id', 'facebook_user', 'phone', 'profile', 'user',)

class EditProfileSerilizer(serializers.ModelSerializer):
    #Update/edit user profile api data formatter.
    class Meta:  #pylint: disable=too-few-public-methods
        # Return optional Profile fields.
        model = Profile
        fields = ('id', 'facebook_user', 'phone', 'profile',)
