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
    bPrice = (bCount//2 * 1.25) + 0.75

    #print(aPrice, bPrice)


    

       




checkoutKata("AAAABBBBBBBCCCCCCCC")   