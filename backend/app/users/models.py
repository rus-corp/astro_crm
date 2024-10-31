from django.db import models

class CustomUser(models.Model):
  login = models.CharField()
  password = models.CharField()
  email = models.EmailField()