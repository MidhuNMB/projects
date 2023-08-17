from django.db import models
class tbl_user(models.Model):
    name=models.CharField(max_length=30)
    phone=models.IntegerField()
    username=models.CharField(max_length=30)
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    class meta:
        db_table='tbl_user'

class cake_tbl(models.Model):
    cakename=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    class meta:
        db_table='cake_tbl'
# Create your models here.