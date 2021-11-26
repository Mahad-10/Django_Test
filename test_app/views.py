from django.http import Http404
from simple_login import views
from test_app.models import User, ImageUpload
from test_app import serializers
from simple_login.views.base import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED


class RegisterAPIView(views.RegisterAPIView):
    serializer_class = serializers.UserSerializer


class LoginAPIView(views.LoginAPIView):
    user_model = User
    serializer_class = serializers.UserSerializer


class ProfileAPIView(views.RetrieveUpdateDestroyProfileAPIView):
    user_model = User
    serializer_class = serializers.UserSerializer


class ImageUploadAPIView(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        try:
            user = self.get_object(self.request.user)
            images = ImageUpload.objects.filter(user=user).all()
            serializer = serializers.ImageUploadSerializer(images, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = self.get_object(self.request.user)
            files = request.FILES.getlist('image')
            for file in files:
                ImageUpload.objects.create(user=user, image=file)
            return Response("Images Uploaded", status=HTTP_200_OK)
        except Exception as e:
            return Response(e, status=HTTP_400_BAD_REQUEST)
