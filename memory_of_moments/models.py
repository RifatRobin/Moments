from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.


class moments(models.Model):
    contents = models.TextField()
    dt = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
