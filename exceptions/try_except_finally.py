try:
    print(a)

except : #ALL EXCEPTIONS ARE ACCEPTED
    print("Program has an exception")

try:
    a = int(input("Give a number:"))
    b = int(input("Give a another number"))
    print(a/b)
except ZeroDivisionError:#SPECIFIC EXCEPTION IS ACCEPTED
    print("A number can not divide zero")

finally:#FINALLY METHOD IS ALWAYS RUNNING.
    print("I am always running")

#OUR EXCEPTIONS...

def reverse_string(string):
    if (type(string) != str):
        raise ValueError("Please give correct input")
    else:
        print(string[::-1])

reverse_string("Eren")
reverse_string(12)


#We can use this exception in try-except
# try:
#     reverse_string(12)
# except:
#     print("Program has an exception")