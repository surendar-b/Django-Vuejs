from django.db import models


class Categorys(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    category = models.CharField(db_column='category',max_length=45)

class Products(models.Model):
    id = models.AutoField(db_column='id',primary_key=True)
    category = models.ForeignKey(Categorys,on_delete=models.CASCADE)
    product_name = models.CharField(db_column='product_name',max_length=60)
    price = models.IntegerField(db_column='price',max_length=5)
# Create your models here.
