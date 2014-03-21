from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    price = models.FloatField()
    minQuantity = models.IntegerField()
    quantity = models.IntegerField()

    def __unicode__(self):
        return "{0:0>4} | {1}".format(self.quantite, self.name)
