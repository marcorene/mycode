#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
#vehicles = { "cars": ["civic", "accord", "lambo"], "trucks": ["F150", "Ram1500", "Sierra"] }
# create a second list of strings
#print(farms["name"][0])
###print(type(farms))
###print(farms[1])
# loop across the list called vendors


for x in farms:
    #print(farms)
    #print(x["name"], " - ", x["agriculture"][0])
    y = 0
    print(x["name"], " - ", x["agriculture"][y])
    print(y)
    ##FUNCIONA IMPRIME TODOS LOS NUMEROS 0
    #print(x["agriculture"][0])
    ##NO FUNCIONAN
    #print(vehicles)
    ###print(x["name"])
    ###print(x["agriculture"])
    #print(vehicles["cars"])
    ##print(vehicles["cars"][2])
    ##print(vehicles["trucks"])
    ##print(vehicles["trucks"][1])

    # newline, print current vendor, and end without newline
    #if x not in approved_vendors:   # if x does not appear within the list approved_vendors
    #    print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished
