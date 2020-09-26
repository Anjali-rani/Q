from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class extendeduser(models.Model):
    college=models.CharField(max_length=255)
    contact=models.CharField(max_length=15)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.college


class Quize(models.Model):
    Roll_No=models.IntegerField(max_length=100)
    Fullname=models.CharField(max_length=255)
    College=models.CharField(max_length=255)
    Mobile=models.CharField(max_length=15)
    TotalMarks=models.CharField(max_length=100)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.Fullname
