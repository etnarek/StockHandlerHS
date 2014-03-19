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
            print("\nHello, que voulez-vous faire?")
            print("P : Connaitre le prix\nG : gérer les stocks\nA : afficher les stocks\n(Rien = acheter)\n")
            choice = raw_input(">> ")
            if len(choice) == 0:
                self.retrieve()
            elif choice[0].upper() == 'P':
                self.getPrix()
                raw_input(">>")
            elif choice[0].upper() == 'G':
                self.manageStock()
            elif choice[0].upper() == 'A':
                self.show()
                raw_input(">>")
            else:
                print("Ce choix n'est pas valide.")
                raw_input(">>")

    def getPrix(self, product = None):
        if product == None:
            product = self.getProduit()
        if product != None:
            print("Un {} coute {} €".format(product.name, product.price))
        else:
            print("Le produit ne se trouve pas dans la base de donnée.")

    def retrieve(self):
        p = self.getProduit()
        if p != None:
            self.getPrix(p)
            print("Voulez-vous acheter? [Y/n]")
            choice = raw_input(">>")
            # TODO: proposer de prendre une quantitée plus grande
            if len(choice) == 0 or choice[0].upper() == "Y":
                try:
                    s = Stock.objects.get(produit=p)
                    s.quantite-=1
                    s.save()
                except:
                    print("{} ne se trouve pas dans la base de donnée des objets stockés.".format(p.name))
            else:
                print("Vous n'avez pas acheté: {}".format(p.name))
        else:
            print("Ce produit n'est pas dans ma base de donnée.")

    def add(self):
        p = self.getProduit()
        if p == None:
            print("Il faut rajouter se produit à la base de donnée.")
            self.new()
        else:
            quantity = raw_input("Quel est la quantitée ajoutée? ")
            s = Stock.objects.get(produit=p)
            s.quantite+=float(quantity)
            s.save()

    def new(self, barcode=""):
        if len(barcode) == 0:
            barcode = self.scan()
        name = raw_input("Entrez le nom du produit: ")
        price = raw_input("Entrez le prix: ")
        quantity = raw_input("Entrez la quantitée: ")
        p = Product(barcode=barcode, name=name, price=price)
        p.save()
        s = Stock(produit=p, quantite=quantity)
        s.save()

    def manageStock(self):
        quit = False
        while not quit:
            os.system("clear")
            print("Comment voulez-vous modifier les stocks?")
            print("N : nouveau produit\nA : augmenter la cantité d'un produit\nQ : quitter\n(Rien = A)")
            choice = raw_input(">> ")
            if len(choice) == 0 or choice[0].upper() == 'A':
                self.add()
            elif choice[0].upper() == 'N':
                self.new()
            elif choice[0].upper() == 'Q':
                quit = True
            else:
                print("Ce choix n'est pas valide.")
                raw_input(">>")

    def scan(self):
        print("Scanning ...")
        self.scanner.process_one()
        print("\a")
        for symbol in self.scanner.results:
            return str(symbol.data)

    def getProduit(self):
        barcode = self.scan()
        try:
            return Product.objects.get(barcode=str(barcode))
        except:
            return None

    def init(self):
        scanner = zbar.Processor()
        scanner.parse_config('enable')
        device = '/dev/video0'
        scanner.init(device)
        scanner.visible = True
        self.scanner = scanner

