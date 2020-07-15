#Advanced Challenge

# Create a list of dictionaries with at least 5 chores in it, using the following format:
# todo = [{"chore": "dishes", "time": 15}, {"chore": "laundry", "time": 20}]
todo = [{"chore": "dishes", "time": 15}, 
        {"chore": "laundry", "time": 20},
        {"chore": "feed dog", "time": 5},
        {"chore": "moping", "time": 25},
        {"chore": "vacuum", "time": 10}]

# Use real values to help you think about your tasks this week.
# Using a for loop, enumerate the list, capturing the index and the value
# https://docs.python.org/3/library/functions.html#enumerate

# Use if/elif/else statement(s) to determine the order of tasks based on their index
# index 0 = first
# index 1 = second
# index 2 = third
# index 3 = fourth
# index 4 = fifth
for x, y in enumerate((todo),1):
    #TO TEST
    #print(x)
    #print(y["chore"], " - ", y["time"])
    if (x) == 1:
        prio = "first"
        #print(y["chore"], " - ", y["time"])
        n = y["chore"]
        m = y["time"]
        print(f"The {prio} thing I have to do is {n}. It should only take {m} minutes.")
    elif (x) == 2:
        prio = "second"
        n = y["chore"]
        m = y["time"]
        print(f"The {prio} thing I have to do is {n}. It should only take {m} minutes.")
    elif (x) == 3:
        prio = "third"
        n = y["chore"]
        m = y["time"]
        print(f"The {prio} thing I have to do is {n}. It should only take {m} minutes.")
    elif (x) == 4:
        prio = "fourth"
        n = y["chore"]
        m = y["time"]
        print(f"The {prio} thing I have to do is {n}. It should only take {m} minutes.")
    else:
        prio = "fifth"
        n = y["chore"]
        m = y["time"]
        print(f"The {prio} thing I have to do is {n}. It should only take {m} minutes.")




# Use this sentence as a guide:
# "The {order of task} thing I have to do is {chore}. It should only take {time} minutes."

# And have your script output 5 such lines:
# "The first thing I have to do is dishes. It should only take 15 minutes."



print("\nOur loop has ended.") # print when loop has finished
