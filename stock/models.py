from django.db import models
from produit.models import Product

# Create your models here.

class Stock(models.Model):
    quantite = models.IntegerField()
    produit = models.ForeignKey(Product)

    def __unicode__(self):
        return "{0:0>4} | {1}".format(self.quantite, self.produit.name)
