from simple_login import views
from test_app.models import User
from test_app import serializers


class RegisterAPIView(views.RegisterAPIView):
    serializer_class = serializers.UserSerializer


class LoginAPIView(views.LoginAPIView):
    user_model = User
    serializer_class = serializers.UserSerializer


class ProfileAPIView(views.RetrieveUpdateDestroyProfileAPIView):
    user_model = User
    serializer_class = serializers.UserSerializer


