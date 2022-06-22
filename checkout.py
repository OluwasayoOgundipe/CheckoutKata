'''Checkout Kata function that implements the proposed supermarket checkout system
   The input to the function is a string of all the items e.g. CCC, ACC
'''

from collections import Counter


def checkoutKata(items):
    items = items.upper()

    itemDict = Counter(items)

    aCount = itemDict["A"]
    bCount = itemDict["B"]
    cCount = itemDict["C"]

    aPrice = aCount * 0.50

    if bCount > 0 and bCount%2 != 0:
        bPrice = (bCount//2 * 1.25) + 0.75

    elif bCount > 0 and bCount%2 == 0:
        bPrice = (bCount/2) * 1.25   

    else:
        bPrice = 0

    cDiscount = cCount//3
    cPrice = (cCount * 0.25) - (cDiscount *0.25)

    print(aPrice, bPrice, cPrice)

    total = aPrice + bPrice + cPrice
    
    print(total)

    return
    



checkoutKata("CCCC")   