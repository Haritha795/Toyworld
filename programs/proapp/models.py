from django.db import models

# Create your models here.

class Message_tbl(models.Model):
    fnm=models.CharField(max_length=25)
    msg=models.CharField(max_length=25)
