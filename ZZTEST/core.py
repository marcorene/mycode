def stringg(word):
    palabra = word.split(" ")
    #print(palabra)
    txt = ""
    VOWELS = ('a', 'e', 'i', 'o', 'u')

    for word in palabra:
        if word.startswith(VOWELS):
            txt += f"{word}ay "
        else:
            txt += f"{word[1:]}{word[:1]}ay "
        return txt
#return palabra

#print(stringg("almost complete this challenge"))