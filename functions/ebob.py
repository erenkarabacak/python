def ebob(number1, number2):
    i = 1
    ebob = 1
    while (i <= number1 and i <= number2):

        if (not (number1 % i) and not (number2 % i)):
            ebob = i
        i += 1
    return ebob


number1 = int(input("number-1:"))
number2 = int(input("number-2:"))

print("Ebob:", ebob(number1, number2))