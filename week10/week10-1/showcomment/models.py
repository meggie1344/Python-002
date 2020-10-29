from django.db import models

# Create your models here.

class Rawdata(models.Model):
    product_title = models.CharField(max_length=100)
    product_comment = models.CharField(max_length=600)

