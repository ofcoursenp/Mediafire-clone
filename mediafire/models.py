from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    file = models.FileField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    


