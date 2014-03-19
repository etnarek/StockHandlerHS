#-*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from produit.models import Product
from stock.models import Stock

import time
import os
import zbar

class Command(BaseCommand):
    help = "Lance le terminal sur le frigo."
    scanner = None

    def handle(self, *args, **options):
        self.init()
        while True:
            os.system("clear")
            print("Hello, que voulez-vous faire?")
            choice = raw_input("P : Connaitre le prix, G : gérer les stocks, A : afficher les stocks, (Rien = acheter) ")
            if len(choice) == 0:
                self.retrieve()
            elif choice[0].upper() == 'P':
                self.getPrix()
            elif choice[0].upper() == 'G':
                self.manageStock()
            elif choice[0].upper() == 'A':
                self.show()
            else:
                print("Ce choix n'est pas valide.")

    def add(self):
        pass

    def getPrix(self, product = None):
        if product == None:
            product = self.scan()
        print("Un {} coute {} €".format(product.name(), product.price()))

    def retrieve(self):
        pass

    def new(self):
        pass

    def dele(self):
        pass

    def manageStock(self):
        pass

    def scan(self):
        print("Scanning ...")
        self.scanner.process_one()
        print("\a")

        for symbol in self.scanner.results:
            return Product.objects.get(barcode=str(symbol.data))

    def init(self):
        scanner = zbar.Processor()
        scanner.parse_config('enable')
        device = '/dev/video0'
        scanner.init(device)
        scanner.visible = True
        self.scanner = scanner

