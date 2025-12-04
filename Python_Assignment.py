# Python Assignment for CFC Workshop.

## Assignment List

# 1. Even or Odd Checker
def even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# 2. Basic Calculator
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"


# 3. Maximum of Three Numbers 
def find_max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# 4. Vowel Counter
def counter_vowels(text):
    count = 0
    for char in text:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count = count + 1
        elif char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U':
            count = count + 1
    return count


# 5. Positive Numbers Filter
def filter_positive_numbers(numbers):
    positives = []
    for num in numbers:
        if num > 0:
            positives.append(num)
    return positives


# 6. Factorial Finder 
    result = 1
    i = 1
    while i <= n:
        result = result * i
        i = i + 1
    return result


# 7. Palindrome Checker
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False


# 8. Pattern Printer
def print_triangle(nums):
    for i in range(1, nums + 1):
        print("*" * i)


# 9. Sum of List Elements
def sumlist(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


# 10. Custom Greeting Function
def custom_greeting(name, time_of_day):
    if time_of_day == "morning":
        return "Good morning, " + name + "!"
    elif time_of_day == "afternoon":
        return "Good afternoon, " + name + "!"
    elif time_of_day == "evening":
        return "Good evening, " + name + "!"
    else:
        return "Hello, " + name + "!"
