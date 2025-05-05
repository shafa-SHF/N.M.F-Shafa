
#Sum the Elements in a List
numbers = [5, 8, 2, 1, 9, 3, 4, 7, 6, 10]
total = 0
for number in numbers:
    total = total + number
print("List of numbers:", numbers)
print("Total sum:", total)




#Add a New Value to a List
fruits = ["apple", "banana", "cherry", "grape", "orange"]
print("Fruit list:", fruits)
print("Fruit at index 2:", fruits[2])
fruits.append("mango")
print("Updated fruit list:", fruits)



#Accept Numbers from the User and Analyze
user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))
total = sum(numbers)
average = total / len(numbers)
largest = max(numbers)
smallest = min(numbers)
print("Numbers:", numbers)
print("Total:", total)
print("Average:", average)
print("Largest:", largest)
print("Smallest:", smallest)



# Calculate Statistics from a List
user_input = input("Enter at least 5 numbers, separated by spaces: ")
numbers = list(map(int, user_input.split()))

minimum = min(numbers)
maximum = max(numbers)
average = sum(numbers) / len(numbers)

sorted_numbers = sorted(numbers)
n = len(sorted_numbers)
if n % 2 == 1:
    median = sorted_numbers[n // 2]
else:
    median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

print("Sorted list:", sorted_numbers)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Median:", median)




# Shopping List Program
shopping_list = []
print("Enter 5 shopping items:")
for i in range(5):
    item = input(f"Item {i + 1}: ")
    shopping_list.append(item)

print("Your shopping list:", shopping_list)

purchased = input("Which item have you purchased? ")
if purchased in shopping_list:
    shopping_list.remove(purchased)

print("Updated shopping list:", shopping_list)

