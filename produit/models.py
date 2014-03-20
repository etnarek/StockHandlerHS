from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    price = models.FloatField()

    def __unicode__(self):
        return self.name
