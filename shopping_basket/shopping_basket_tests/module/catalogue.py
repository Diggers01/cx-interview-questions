# Catalogue class
# Author : Digby Marsh
# Email : digby.j.marsh@gmail.com
# Date : 2021/01/30

class Catalogue():
    _instance = None

    # Create a new instance or load instance already created
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Catalogue, cls).__new__(cls)
            cls.currentCart = {}
            # Put any initialization here.
        return cls._instance

    # getItems - Get the catalogue items 
    def getItems(self):
        return {
            0 : {
                "name" : "Baked Beans",
                "price" : 0.99
            },
            1 : {
                "name" : "Biscuits",
                "price" : 1.20
            },
            2 : {
                "name" : "Sardines",
                "price" : 1.89
            },
            3 : {
                "name" : "Shampoo (Small)",
                "price" : 2.00
            },
            4 : {
                "name" : "Shampoo (Medium)",
                "price" : 2.50
            },
            5 : {
                "name" : "Shampoo (Large)",
                "price" : 3.50
            }
        }
    
    # getItem - Get information about the item selected
    # Param : id - Item ID
    # return array of specific item
    def getItem(self, id):
        items = self.getItems()
        return items[id]
    
    # addToBasket - Add an item to the basket
    # Param : id - Item ID
    def addToBasket(self, id):
        if id in self.currentCart :
            self.currentCart[id] = self.currentCart[id] + 1
        else :
            self.currentCart[id] = 1

    # getBasket - Get current basket
    # return basket content
    def getBasket(self):
        return self.currentCart

    # resetBasket - Resets the users basket
    def resetBasket(self):
        self.currentCart = {}