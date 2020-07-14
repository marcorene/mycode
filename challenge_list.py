# Create a dictionary with 2 keys, pets and movies
# Have the value of pets be a list of dictionaries with keys of "type" and "name"
# Have the value of movies be a list of dictionaries with keys of "rating" and "name"
# pets and movies should have 3 items each
challenge = {
    "pets": [{"type": "dog", "name": "chester"}, {"type": "cat", "name": "daisy"}, {"type": "bird", "name": "tom"}], 
    "movies": [{"rating": "PG13", "name": "scary movie"}, {"rating": "R", "name": "Gladiator"}, {"rating": "G", "name": "Toy Story"}]
}


# print out 2 of pets with their type and name
print(challenge["pets"][0])
print(challenge["pets"][2])
# print out 1 movie with its rating and name
print(challenge["movies"][2])

#as intructor
# print out 2 of pets with their type and name
print(challenge["pets"][0]["type"])
print(challenge["pets"][0]["name"])

print(challenge["pets"][2]["type"])
print(challenge["pets"][2]["name"])
# print out 1 movie with its rating and name
print(challenge["movies"][1]["rating"])
print(challenge["movies"][1]["name"])

