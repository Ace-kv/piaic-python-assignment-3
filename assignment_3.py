# Instructions: Implement Python programs to accomplish the following task

# Task

# You are tasked with creating a Python program that serves as an interactive tool for a friend who enjoys exploring numbers.
# The program should begin by prompting the user to enter their name and then ask them for three of their favorite numbers. 
# After gathering this information, the program should greet the user with a personalized message that includes their name. 
# The three numbers provided by the user should be stored in a list. The program should then check if any of the numbers 
# are even or odd, and store this information in a separate list of tuples, where each tuple contains the number and a string 
# indicating whether it is "even" or "odd". Following this, the program should use a for loop to iterate over the list of numbers, 
# and for each number, it should create a tuple containing the number and its square. These tuples should be printed in a 
# creative and engaging format. Additionally, the program should calculate the sum of the three numbers and print the result, 
# accompanied by an encouraging message. Finally, the program should determine if the sum is a prime number and notify the user 
# with an appropriate message. The goal is to make the tool both enjoyable and informative, allowing the user to explore their 
# favorite numbers in a fun and interactive way, while also introducing some interesting logical checks.

# Example Output:

# Enter your name: Alex
# Enter your first favorite number: 4
# Enter your second favorite number: 6
# Enter your third favorite number: 9

# Hello, Alex! Let's explore your favorite numbers:
# The number 4 is even.
# The number 6 is even.
# The number 9 is odd.
# The number 4 and its square: (4, 16)
# The number 6 and its square: (6, 36)
# The number 9 and its square: (9, 81)

# Amazing! The sum of your favorite numbers is: 19
# Wow, 19 is a prime number!

name: str = input("Enter your name: ")

first_num: int = int(input("\nEnter your first favorite number: "))
second_num: int = int(input("Enter your second favorite number: "))
third_num: int = int(input("Enter your third favorite number: "))

print(f"\nHello {name}! Let's explore your favorite numbers:\n")

num_list: list[int] = [first_num, second_num, third_num]

num_tuple_list: list[tuple[int, str]] = []
for num in num_list:
    if num % 2 == 0:
        print(f"The number {num} is even.")
        num_tuple_list.append((num, "even"))
    else:
        print(f"The number {num} is odd.")
        num_tuple_list.append((num, "odd"))

print("\n")

num_tuple: tuple[int, int]
for num in num_list:
    num_tuple = (num, num ** 2)
    print(f"The number {num} and its square: {num_tuple}")

num_sum = sum(num_list)
print(f"\nAmazing! The sum of your favorite numbers is: {num_sum}\n")

import math

# Negative numbers, 0, and 1 are not primes
if num_sum > 1:
  
    for i in range(2, int(math.sqrt(num_sum)) + 1):
      
        if (num_sum % i) == 0:
            print(num_sum, "is not a prime number")
            break

    else:
        print("And", num_sum, "is a prime number!")
else:
    print(num_sum, "is not a prime number")
