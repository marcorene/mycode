car_list = ["BMW", "Audi", "Mercedes", "Ford", "Chevrolet"]
name_list = ["Marco", "Sam", "Sean", "Adrise", "Omar"]
print(car_list[3])
print(name_list[3])
print(car_list[2:5])
print(name_list[-5:-3])
combined_list = []
#print(combined_list)
combined_list.append(car_list)
#print(combined_list)
combined_list.extend(name_list)
print(combined_list)
#Now, try to print out Audi and Ford from the combined list, and Sam and Marco from there as well
print(combined_list[0][1])
print(combined_list[0][3])
print(combined_list[2])
print(combined_list[1])
print ("OR")
print (combined_list[2], combined_list[1])
print ("OR")
my_str = combined_list[2] + ' is less cooler than ' + combined_list[1]
print (my_str)
better= "{} is better than {}".format(combined_list[4], combined_list[2])
print (better)
combined_list.reverse()
print(combined_list)