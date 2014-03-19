class Produit:
    def __init__(self,name,barcode,price):
        self.name = name
        self.barcode = barcode
        self.price = price
    def __repr__(self):
        string = "Product name : {0}, Barcode : {1}, Price : {2} ".format(self.name, str(self.barcode), str(self.price))
        return string 
    def __str__(self):
        return self.__repr__()

    def qprint(self,quantity):
        print "Product name : {0}, Barcode : {1}, Quantity : {3}, Price : {2} ".format(self.name, str(self.barcode), str(self.price),str(quantity))
