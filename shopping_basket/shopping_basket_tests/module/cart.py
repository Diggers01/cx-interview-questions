# Cart class
# Author : Digby Marsh
# Email : digby.j.marsh@gmail.com
# Date : 2021/01/30

from module.catalogue import *
from decimal import Decimal
import math

class Cart():
    TwoGetOneFreeSeparator = "|"
    
    # Class initialization
    def __init__(self):
        self.catalogue = Catalogue()

    # buyTwoGetOneFree - Add item ID to the discounts
    # Param : id - Item ID
    def buyTwoGetOneFree(self, id):
        if id not in self.discounts["TGOF"] :
            self.discounts["TGOF"][id] = 1

    # buyXGetCheapestFree - Adds Items that will have the discount effect
    # Param : number - Number of different items in the offer
    # Param : ids - Array of item IDs which will have the discount
    def buyXGetCheapestFree(self, number, ids):
        idsText = self.TwoGetOneFreeSeparator.join(ids)
        if idsText not in self.discounts["TCF"] :
            self.discounts["TCF"][idsText] = {
                'number' : number,
                'ids' : ids
            }

    # addDiscount - Add item ID to the discounts
    # Param : id - Item ID
    # Param : percentage - Percentage discount
    def addDiscount(self, id, percentage):
        if id not in self.discounts["D"] :
            self.discounts["D"][id] = percentage

    # resetOffers - remove all current offers
    def resetOffers(self):
        self.discounts = {
            'TGOF':{},
            'TCF':{},
            'D':{},
        }

    # firstOffer - Setting first discount offers
    def firstOffer(self):
        self.resetOffers()
        self.buyTwoGetOneFree(0)
        self.addDiscount(2, 25)

    # secondOffer - Setting secound discount offers
    def secondOffer(self):
        self.resetOffers()
        self.buyXGetCheapestFree(3, {"3":1,"4":1,"5":1})

    # bothOffer - Setting both discount offers
    def bothOffer(self):
        self.resetOffers()
        self.buyTwoGetOneFree(0)
        self.addDiscount(2, 25)
        self.buyXGetCheapestFree(3, {"3":1,"4":1,"5":1})

    # calculateCart - Calculate cart information 
    # return subprice and discount amount
    def calculateCart(self):
        currentBasket = self.catalogue.getBasket()
        items = self.catalogue.getItems()
        subPrice = Decimal('0.00')
        discount = Decimal('0.00')
        excessTCF = {}
        for itemID in currentBasket:
            TGOFDiscount = 0
            DDiscount = 0
            subPrice += (Decimal(items[itemID]["price"]) * currentBasket[itemID])
            # Check if the item has a 2 for 1 discount
            if itemID in self.discounts["TGOF"] and math.floor(currentBasket[itemID] / 3) >= 1 :
                TGOFDiscount = 1
                discount += Decimal(math.floor(currentBasket[itemID] / 3) * Decimal(items[itemID]["price"]))
            # Check if the item has a percentage discount
            elif itemID in self.discounts["D"] :
                DDiscount = 1
                discount += Decimal(math.ceil((items[itemID]["price"] * currentBasket[itemID]) / (100 / self.discounts["D"][itemID])* 100) / 100)
            # Check if discount buy 3 get cheapest for free 
            if TGOFDiscount > 0 or DDiscount > 0:
                for id in self.discounts["TCF"] :
                    if id not in excessTCF :
                        excessTCF[id] = {
                            'maxItems' : 0,
                            'items' : {}
                        }
                    excessTCF[id]['maxItems'] = self.discounts["TCF"][id]['number']
                    stringItemID = str(itemID)
                    if stringItemID in self.discounts["TCF"][id]['ids'] and math.floor(currentBasket[itemID] / 3) >= 1 :
                        discount += Decimal(math.floor((currentBasket[itemID] / 3)) * Decimal(items[itemID]["price"]))
                        excessTCF[id]['items'][itemID] = {
                            'count' : currentBasket[itemID] - (math.floor(currentBasket[itemID] / 3) * 3 ),
                            'price' : items[itemID]['price']
                        }
                        
                    elif stringItemID in self.discounts["TCF"][id]['ids']:
                        excessTCF[id]['items'][itemID] = {
                            'count' : currentBasket[itemID],
                            'price' : items[itemID]['price']
                        }

        # discount = Decimal(self.findDiscounts(items, excessTCF, discount))
        return {
            'subPrice' : subPrice,
            'discount' : discount
        }
    
    def findDiscounts(self, items, excess, discount):
        print(excess)
        for id in excess:
            NumberItems = 0
            propertise = {}
            for i in range(0, excess[id]["maxItems"], 1):
                propertise[i] = {
                    'price' : Decimal('inf'),
                    'itemId' : 0,
                    'number' : 0
                }
            for itemID in excess[id]['items']:
                for i in range(0, excess[id]["maxItems"], 1):
                    if propertise[i]['price'] > Decimal(excess[id]['items'][itemID]["price"]):
                        propertise[i]['price'] = Decimal(excess[id]['items'][itemID]["price"])
                        propertise[i]['itemId'] = itemID
                        propertise[i]['number'] = excess[id]['items'][itemID]['count']
                        break    

                NumberItems += excess[id]['items'][itemID]["count"]
            if NumberItems >= excess[id]["maxItems"]:
                print(5555555)
                # discount += self.findDiscounts(items, excess, discount)
            print(propertise)
        return discount

    

