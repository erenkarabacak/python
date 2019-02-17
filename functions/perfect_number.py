
number = int(input("Give a number:"))
def perfect_number(x):
    total = 0;
    for i in range(1,x):
        if x % i == 0:
            total += i;

    if total == x:
        print(x,"is a perfect number")
    else:
        print(x,"is not a perfect number")

perfect_number(number)
