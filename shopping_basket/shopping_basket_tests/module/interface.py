# Interface class
# Author : Digby Marsh
# Email : digby.j.marsh@gmail.com
# Date : 2021/01/30

from tkinter import *
from module.catalogue import *
from module.cart import *

class Interface():

    # Class initialization
    # Param : window - TK window
    # Param : page - 
    def __init__(self, window):
        super().__init__()
        self.catalague_rows = 2
        self.catalague_columns = 3
        self.catalogue = Catalogue()
        self.cart = Cart()
        self.catalogue_list = self.catalogue.getItems()
        self.frame = Frame(window)
        self.window = window
        self.initCatalogue()
        self.cart.firstOffer()

    # initCatalogue - displays catalogue interface
    def initCatalogue(self):

        self.frame.pack(fill=BOTH, expand=True)

        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(3, pad=7)
        self.frame.rowconfigure(4, weight=1)
        self.frame.rowconfigure(5, pad=7)

        lbl = Label(self.frame, text="Catalogue")
        lbl.grid(sticky=W, pady=4, padx=5)


        cartButton = Button(self.frame, text="Cart", command = self.basketPage)
        cartButton.grid(row=0, column=3)

        resetButton = Button(self.frame, text="Reset Cart", command = self.resetBasket)
        resetButton.grid(row=1, column=3)

        resetButton = Button(self.frame, text="First test Offer", command = self.cart.firstOffer)
        resetButton.grid(row=4, column=0)
        resetButton = Button(self.frame, text="Second test Offer", command = self.cart.secondOffer)
        resetButton.grid(row=4, column=1)
        resetButton = Button(self.frame, text="Both test Offer", command = self.cart.bothOffer)
        resetButton.grid(row=4, column=2)

        for i in range(0, self.catalague_rows * self.catalague_columns, 1):
            abtn = Button(self.frame, text=self.catalogue_list[i]["name"]+"\n£"+str(self.catalogue_list[i]["price"]), width=30, pady=30, command=lambda i=i: self.addToBasket(i))
            abtn.grid(row=(i%self.catalague_rows) + 1, column=i%self.catalague_columns)

    # initCart - displays cart interface
    def initCart(self): 
        self.frame.pack(fill=BOTH, expand=True)

        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(3, pad=7)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(5, pad=7)

        lbl = Label(self.frame, text="Cart")
        lbl.grid(sticky=W, pady=4, padx=5)

        abtn = Button(self.frame, text="Catalogue", command = self.cataloguePage)
        abtn.grid(row=0, column=2)

        basket = self.getBasket()
        items = []
        separator = "\n"
        for itemID in basket:
            item = self.catalogue.getItem(itemID)
            items.append(item["name"] + " x " + str(basket[itemID]))
        basketDisplay = Label(self.frame, text=separator.join(items))
        basketDisplay.grid(row=1, column=0)
        
        cartResultsData = self.cart.calculateCart()
        text = "sub-total: £" + str('{:.2f}'.format(cartResultsData['subPrice'])) + "\ndiscount: £" + str('{:.2f}'.format(cartResultsData['discount'])) + "\ntotal: £" + str('{:.2f}'.format(cartResultsData['subPrice'] - cartResultsData['discount']))
        basketDisplay = Label(self.frame, text=text)
        basketDisplay.grid(row=1, column=1)

    # basketPage - Change the interface to the basket page
    def basketPage(self):
        self.frame.destroy()
        self.frame = Frame(self.window)
        self.initCart()

    # cataloguePage - Change the interface to the catalogue page
    def cataloguePage(self):
        self.frame.destroy()
        self.frame = Frame(self.window)
        self.initCatalogue()
        
    # addToBasket - Add item to the basket
    # Param : id - ID of the item
    def addToBasket(self, id):
        self.catalogue.addToBasket(id)

    # getBasket - Get the basket content 
    # return : basket items
    def getBasket(self):
        return self.catalogue.getBasket()

    # resetBasket - Reset user basket
    def resetBasket(self):
        self.catalogue.resetBasket()
