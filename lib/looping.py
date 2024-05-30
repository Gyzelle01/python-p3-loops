#!/usr/bin/env python3

# Function to countdown and print Happy New Year
def happy_new_year():
    countdown = 10
    while countdown in range(10, 0, -1):  # Loop from 10 to 0 in reverse order
        print(countdown)
        countdown -= 1
    
    print("Happy New Year!")

# Function to square all integers in a list
def square_integers(int_list):
    return [i ** 2 for i in int_list]  # List comprehension to square each integer in the input list

# Function to print FizzBuzz numbers
def fizzbuzz():
    for i in range(1, 101):  # Loop from 1 to 100
        if not i % 15:  # Check if the number is divisible by 15
            print("FizzBuzz")
        elif not i % 5:  # Check if the number is divisible by 5
            print("Buzz")
        elif not i % 3:  # Check if the number is divisible by 3
            print("Fizz")
        else:  # If none of the above conditions are met, print the number itself
            print(i)