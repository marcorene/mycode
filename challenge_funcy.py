# Create 3 functions
# A math function that takes 2 required arguments, multiplies them together, and then divides by 100
#     and returns the result

def math (n1, n2):
    res = (n1 * n2) / 100
    #print (res)
    return res

#math(10, 10)

# A stringy function that takes a required argument string and returns every other letter from the string
def stringy (txt):
    wordlist = list(txt)
    #print(wordlist)
    tlet=(len(wordlist))
    i=0
    while i < tlet:
        #print(wordlist[i])
        accum = print(wordlist[i])
        i += 1
    return accum
#print(stringy("oso"))
# A main function that calls on both of these previous functions, which has 1 required argument of an integer, and has two default arguments (1 int and 1 string)
def main (m1, m2=10, m3="Pennsylvania"):
    print(math(m1, m2))
    print(stringy(m3))
    return
# Call on the main function
main(50)