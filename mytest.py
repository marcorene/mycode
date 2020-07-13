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
print(combined_list[0][1])
print(combined_list[0][3])
print(combined_list[2])
print(combined_list[1])