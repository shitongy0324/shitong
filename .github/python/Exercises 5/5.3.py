def integer_number(number):
    if number < 2:
        return False
    for i in range(2, number + 1):
        if number % i == 0:
            return False
    return True


user_number = int(input("enter an integer"))
if integer_number(user_number):
    print("it is a prime number")
else:
    print("it is not a prime number")
