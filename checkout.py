'''Checkout Kata function that implements the proposed supermarket checkout system
   The input to the function is a string or list of all the items e.g. CCC, ACC, BBCCC
   It then returns the total price
'''

from collections import Counter #Counter class to create a frequency dictionary


def checkoutKata(items):
    items = items.upper() #handling lowercase scenarios

    itemDict = Counter(items) #using the counter class to create the frequency dictionary


    #retrieving the number of each item from the frequency dictionary
    aCount = itemDict["A"]
    bCount = itemDict["B"]
    cCount = itemDict["C"]

    aPrice = aCount * 0.50

    if bCount > 0 and bCount%2 != 0: #handling when number of item B is odd
        bPrice = (bCount//2 * 1.25) + 0.75

    elif bCount > 0 and bCount%2 == 0: # handling when number of item b is even
        bPrice = (bCount/2) * 1.25   

    else:
        bPrice = 0

    if cCount > 3:
        cDiscount = cCount//3
        cPrice = (cCount * 0.25) - (cDiscount * 0.25) #creating the discount for item c

    else:
        cPrice = cCount * 0.25    

    total = aPrice + bPrice + cPrice
    ans = "£" + str(total)
    
    print("Your total is: ",ans)

    return total
    
    
checkoutKata("CCC")   