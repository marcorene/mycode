# Handling Errors Challenge

# Create a function that takes a required argument of a list, and an optional parameter of an integer 
#def test1(a="cats", b=24, c="lizard", d=7, e="fish", f=300):
def test1(mylist):
    #thislist = list((a, b, c, d, e, f))
    #thislist = [test1]
    #print(type(test1))

    try:
        for i in mylist:
            print(i)
            res = i / 2
            print("Value divided by 2 is =", res)
        return i
    except TypeError:
        print("Your item", i, "is not divisible by 2 ")
        return i
# Iterate through each item of the list
# Use a try/except block to "try" to divide each item by your optional integer parameter
# If there is a ValueError, handle it by printing out the value of the error (err) and also printing "Your item ____ is not divisible by ____ " (fill in with item of list, and optional integer)
# Execute the function

# Use the list below (or one like it) to accomplish this task
#mixed = ["cats", 24, "lizards", 7, "fish", 300]
print(test1([10, 24, "lizards", 7, "fish", 300]))
#print(test1([2, 24, 20, 7, 10, 300]))