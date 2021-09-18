from django.db import models
from simple_login import models as dsl_models


class User(dsl_models.BaseUser):
    username = models.CharField(max_length=255, unique=True,)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)


