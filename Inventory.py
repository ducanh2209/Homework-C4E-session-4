inventory = {

    "gold" : 500 ,
    "pouch" : [ "flint" , "twine" , "gemstone" ] ,
    "backpack" : [ "xylophone" , "dagger" , "bedroll" , "bread loaf" ]

}
print ("> Here is my Inventory: ", inventory)
inventory["pocket"] = ["seashell" , "strange berry" , "lint" ]
print ("> Here is my inventory + pocket: ", inventory)
inventory["backpack"].sort()
print ("Hmm, I should sort my backpack")
print ("> Did it", inventory["backpack"])
inventory["backpack"].remove("dagger")
print ("I dont need this dagger, better throw it away")
print ("> Nice and clear. This is my new backpack: ", inventory["backpack"])
inventory["gold"] += 50
print ("Yay, found a tresure !")
print ("> Now I have {0} money", format(inventory["gold"]))
