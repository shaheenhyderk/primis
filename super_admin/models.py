from django.db import models


# Create your models here.
class Admin:
    name = models.CharField()
    username = models.CharField()
    email = models.CharField()
