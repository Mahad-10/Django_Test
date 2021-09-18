from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from test_app.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'date_of_birth', 'date_joined')
