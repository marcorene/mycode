#!/usr/bin/env python3

# create a list called list1
list1 = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow"]
# display list1
print(list1)
# display list1[1] which should only display arista_eos
print(list1[1])
# create a new list containing a single item
list2 = ["Kit"]
# extend list1 by list2 (combine both lists together into a single list)
list1.extend(list2)
# display list1, which now contains juniper
print(list1)
# create list3
list3 = ["Jay", "Hog", "Hen"]
# use the append operation to append list1 by list3
list1.append(list3)
# display the new complex list1
print(list1)
# display the list of IP addresses
print(list1[10])
# display the first item in the list (0th item) - first IP address
print(list1[10][1])

