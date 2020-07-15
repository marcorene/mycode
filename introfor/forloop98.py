#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    y = 0
    while y < len(x["agriculture"]):
       print(x["name"], " - ", x["agriculture"][y])
       y += 1
print("\nOur loop has ended.") # print when loop has finished
