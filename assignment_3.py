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
