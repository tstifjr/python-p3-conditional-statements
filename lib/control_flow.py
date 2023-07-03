#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    pass
    if username.lower() == "admin" and password == '12345' :
        return "Access granted"
    else : return "Access denied"

def hows_the_weather(temperature):
    # your code here
    pass
    if(temperature < 40) : return "It's brisk out there!"
    if( 65 > temperature > 40) : return "It's a little chilly out there!"
    if(temperature > 85) : return "It's too dang hot out there!"
    else : return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    pass
    if (num % 3 == 0 and num % 5 == 0) : return "FizzBuzz"
    if (num % 3 == 0) : return "Fizz"
    if (num % 5 == 0) : return "Buzz"
    else : return num

def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == "+" : 
        return num1 + num2
    elif operation == "-" :
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else : 
        print("Invalid operation!")
        return None

print (3 % 3)
print (0 % 3)