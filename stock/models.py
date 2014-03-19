from django.db import models
from produit.models import Product

# Create your models here.

class Stock(models.Model):
    quantite = models.IntegerField()
    produit = models.ForeignKey(Product)
