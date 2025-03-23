from datetime import datetime

# Given data
data = [
    {"name": "Nugraha", "birthdate": "1989-09-13"},
    {"name": "John", "birthdate": "1990-01-01"},
    {"name": "Jane", "birthdate": "1992-02-02"},
    {"name": "Doe", "birthdate": "1994-03-03"}
]

# Function to calculate age
def get_age(birthdate):
    year = int(birthdate[:4])  # Extract year from birthdate
    return datetime.today().year - year

# Print table
print("No | Name     | Age")
print("-------------------")
for i, person in enumerate(data, 1):
    print(f"{i}  | {person['name']:<8} | {get_age(person['birthdate'])}")



# Deret 1: 50, 48, 44, 38, 30, 20, 8, -6
deret1 = []
num = 50
steps = [2, 4, 6, 8, 10, 12, 14]  # Pattern of decreasing steps

for step in steps:
    deret1.append(num)
    num -= step

print("Deret 1:", ", ".join(map(str, deret1)))


# Deret 2: Fibonacci sequence starting from 2, 3
deret2 = [2, 3]

for _ in range(6):  # Generate the next 6 numbers
    deret2.append(deret2[-1] + deret2[-2])

print("Deret 2:", ", ".join(map(str, deret2)))



# Deret 3: 40, 39, 36, 31, 24, 15, 4, -9
deret3 = []
num = 40
steps = [1, 3, 5, 7, 9, 11, 13]  # Decreasing steps pattern

for step in steps:
    deret3.append(num)
    num -= step

print("Deret 3:", ", ".join(map(str, deret3)))



# Deret 4: 100, 99, 96, 91, 84, 75, 64, 51
deret4 = []
num = 100
steps = [1, 3, 5, 7, 9, 11, 13]  # Decreasing steps pattern

for step in steps:
    deret4.append(num)
    num -= step

print("Deret 4:", ", ".join(map(str, deret4)))




# Deret 5: Fibonacci sequence starting from 1, 1
deret5 = [1, 1]

for _ in range(6):  # Generate the next 6 numbers
    deret5.append(deret5[-1] + deret5[-2])

print("Deret 5:", " ".join(map(str, deret5)))

