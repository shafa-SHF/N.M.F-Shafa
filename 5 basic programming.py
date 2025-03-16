#Create a program that takes a number as input and prints"Positive" if the number is greater than zero, and "Negative" if the number is less than zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Problem 2 Create a program to determine whether a number entered by the user is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# Create a program that takes a test score (0-100) as input and determines the grade according to the following criteria
score = int(input("Enter the test score (0-100): "))
if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score <= 79:
    print("Grade: B")
elif 60 <= score <= 69:
    print("Grade: C")
elif 50 <= score <= 59:
    print("Grade: D")
elif 0 <= score <= 49:
    print("Grade: E")
else:
    print("Invalid score! Please enter a number between 0 and 100.")


# Create a program that takes three numbers as input and displays the largest of the three numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
print("The largest number is:", largest)


#Create a program to determine whether a year entered by the user is a leap year or not. A leap year is a year that is divisible by 4, but not divisible by 100, unless the year is divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")


# Create a simple calculator program that takes two numbers and one operator (+, -, *, /)
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    print("Result:", num1 + num2)
elif operator == '-':
    print("Result:", num1 - num2)
elif operator == '*':
    print("Result:", num1 * num2)
elif operator == '/':
    # Check for division by zero
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")


# Get user input for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif 18.5 <= bmi < 25.0:
    category = "Normal"
elif 25.0 <= bmi < 30.0:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is: {bmi:.2f}")
print(f"You are classified as: {category}")


 #Create a program to check if three entered numbers can form a triangle. If so, determine the type of triangle (equilateral, isosceles, or scalene).
# Get user input for three sides of the triangle
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

# Check if the three sides can form a triangle
if a + b > c and a + c > b and b + c > a:
    print("The given sides form a triangle.")

    # Determine the type of triangle
    if a == b == c:
        print("It is an Equilateral triangle.")
    elif a == b or a == c or b == c:
        print("It is an Isosceles triangle.")
    else:
        print("It is a Scalene triangle.")
else:
    print("The given sides do NOT form a triangle.")



#Create a program that simulates a simple login system. The program takes username and password input, then checks the following combinations
# Get user input for username and password
username = input("Enter username: ").strip()
password = input("Enter password (leave blank if none): ").strip()

# Check login credentials
if username == "admin" and password == "admin123":
    print("Access Granted: Admin Access")
elif username == "user" and password == "user123":
    print("Access Granted: Limited Access")
elif username == "guest" and password == "":
    print("Access Granted: Minimal Access")
else:
    print("Access Denied: Invalid Credentials")



#Create a program for the rock-paper-scissors game. The program takes the player's choice as input, then the computer chooses randomly. The program determines the winner based on the rules   
import random

choices = ["rock", "paper", "scissors"]

while True:
    player = input("Enter rock, paper, or scissors (or 'quit' to stop): ").lower()
    if player == "quit":
        break

    if player not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

