from django.db import models

# Create your models here.
class Reg_tbl(models.Model):
    fnm=models.CharField(max_length=25)
    mob = models.CharField(max_length=16)
    eml=models.EmailField()
    psw=models.CharField(max_length=16)

class Task(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class status(models.Model):
    pname=models.CharField(max_length=25)
    rdate=models.DateField()
    ssmry=models.TextField()
    issues=models.TextField()
    update=models.DateField()
