from django.db import models
from simple_login import models as dsl_models


class User(dsl_models.BaseUser):
    username = models.CharField(max_length=255, unique=True,)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    email = models.EmailField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)


class ImageUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    creation_date = models.DateTimeField(auto_now_add=True)


