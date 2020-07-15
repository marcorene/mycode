#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    #print(farms)
    #print(x["name"], " - ", x["agriculture"][0])
    #$y = len(x["agriculture"])
    #$y = -1
    #$print(x["name"], " - ", x["agriculture"][y])
    #$print(y)
    y = 0
    #while y < 3:
    while y < len(x["agriculture"]):
       print(x["name"], " - ", x["agriculture"][y])
       #print(y)
       y += 1
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
