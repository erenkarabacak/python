import math

print("********************** Calculator *****************")
print("1-addition\n2-substraction\n3-multiply\n4-division\n5-squareroot\n6-cosx\n7-sinx\n8-tanx\n9-factorial\n10-n_power")

operation = int(input("Which operation do you want to use: "))

if operation == 1:
    total = 0;
    while True:
        print("If you want the see result, please give 0")
        number = int(input("numbers:"))
        total = total + number;
        if number == 0:
            break
    print("Result: ",total)

elif operation == 2:
    total = 0;

    number1 = int(input("number1: "))
    total = number1
    while True:
        print("If you want the quit, please give 0")
        number2 = int(input("number2: "))
        total = total - number2;

        print("Result: ",total)

        if number2 == 0:
            break
elif operation == 3:
    total = 0;

    number1 = int(input("number1: "))
    total = number1
    while True:
        print("If you want the quit, please give 0")
        number2 = int(input("number2: "))
        total = total * number2;

        print("Result: ",total)

        if number2 == 0:
            break

elif operation == 4:
    total = 0;

    number1 = int(input("number1: "))
    total = number1
    while True:
        print("If you want the quit, please give 0")
        number2 = int(input("number2: "))
        total = total / number2;

        print("Result: ",total)

        if number2 == 0:
            break

elif operation == 5:


    number1 = int(input("number: "))
    print("squareroot {0} is {1}".format(number1,math.sqrt(number1)))

elif operation == 6:


    number1 = int(input("number: "))
    print("cos {0} is {1}".format(number1,math.cos(number1)))

elif operation == 7:


    number1 = int(input("number: "))
    print("sin {0} is {1}".format(number1,math.sin(number1)))

elif operation == 8:


    number1 = int(input("number: "))
    print("tan {0} is {1}".format(number1,math.tan(number1)))

elif operation == 9:


    number1 = int(input("number: "))
    print("factorial {0} is {1}".format(number1,math.factorial(number1)))


elif operation == 10:


    number1 = int(input("number: "))
    power = int(input("power:"))
    print("{0} power {1} is {2}".format(number1,power,math.pow(number1,power)))