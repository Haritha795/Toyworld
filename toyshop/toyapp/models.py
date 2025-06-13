from django.db import models

# Create your models here.
class Reg_tbl(models.Model):
    fnm=models.CharField(max_length=25)
    mob = models.CharField(max_length=16)
    eml=models.EmailField()
    psw=models.CharField(max_length=16)

class toy_tbl(models.Model):
    tname=models.CharField(max_length=25)
    tprc=models.IntegerField()
    timg=models.FileField(upload_to='pic')
    desc=models.TextField()

class cart_tbl(models.Model):
    product=models.ForeignKey(toy_tbl,on_delete=models.CASCADE)
    customer=models.ForeignKey(Reg_tbl,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)
    