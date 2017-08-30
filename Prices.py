prices = {
     "banana" : 4 ,
    "apple" : 2 ,
    "orange" : 1.5 ,
    "pear" : 3

}

purchased_items = [
    {
        "banana" : 5
    },
    {
        "orange" : 3
    }
]
total = 0
for item in purchased_items :
    for pop in item :
        print ( "{0}, quantity: {1}, unit price: {2}".format( pop, item[pop], prices[pop] ) )
        purchased_item = item[pop] * prices[pop]
        print("The amount of {0} money you have to pay is: {1}$".format( pop, purchased_item ))
        total += purchased_item
        print("Thank you for your purchase. See you next time")


