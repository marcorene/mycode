#!/usr/bin/env python3
#A program that prompts the user for a value (1 through n), then returns a quick synopsis of a book or movie in that series.
#Harry Potter
#Hobbit & Lord of the Rings
#Chronicles of Narnia
#Indiana Jones
movie='"Choose with a number the movie that you want to know about"'
movie1= '1. Harry Potter'
movie2= '2. Hobbit & Lord of the Rings'
movie3= '3. Chronicles of Narnia'
movie4= '4. Indiana Jones'
message = 'synopsis: '

print(movie)
print(movie1)
print(movie2)
print(movie3)
print(movie4)
# wrap connection in a float() to accept decimals as numbers
Movie_option = float(input("input the number: "))

# if input value was higher or equal to 25
if Movie_option == 1:
    resume = movie1, message + 'Adaptation of the first of J.K. Rowling popular children novels.'
elif Movie_option == 2:
    resume = movie2, message + 'Bilbo Baggins is a hobbit who lives a quiet life, until it is upset by a visit from a wizard named Gandalf.'
elif Movie_option == 3:
    resume = movie3, message + 'During the World War II bombings of London, four English siblings are sent to a country house where they will be safe'
else:
    resume = movie4, message + 'Epic tale in which an intrepid archaeologist tries to beat a band of Nazis to a unique religious relic which is central to their plans for world domination'
print(resume)

