#1.Create an application to calculate the area of a square
Side= float(input ("Enter the length of a side  : "))
Area = Side*Side
print('The Area of the square is ', Area)

#2.Create an application to calculate the change based on the total purchase and the amount paid
total_purchase =float(input("Enter the total purchase amount : "))
Amount_paid = float(input("Enter the amount paid: "))
Change= Amount_paid - total_purchase
print('Change to be given is ', Change)

#3.Create an application to calculate the total payment after a 20% discount.
Total_purchase= float(input("Enter the total purchase amount: "))
Discount = Total_purchase * (20/100)
Total_payment = Total_purchase - Discount
print("Total purchase amount: $",round(Total_purchase,2))
print("Discount 20%: ",round(Discount,2))
print("The total payment is: $",round(Total_payment,2))

#4.Create an application to calculate the profit earned based on sheep sales, where the base price is 2,500,000 and the selling price is 3,000,000. Calculate the total capital spent and the profit obtained for the number of sheep entered.
Sheep= float(input("Number of sheep :"))
Base_price = 2500000
Selling_price = 3000000
total_capital_spent = Sheep * Base_price
total_profit = (Sheep*Selling_price) - (Sheep*Base_price)
print('the total capital spent is: Rp',total_capital_spent)
print('the total profit is : RP',total_profit)

#5.Create a program that swaps the values of two variables without using an additional variable (use x and y).
X = float(input ("Enter the x value : "))
Y= float(input("Enter the Y value : "))
X,Y = Y,X
print("X is",X)
print("Y is",Y)

#6.Calculate the average of three numbers
A= float(input("Enter a number: "))
B=float(input("Enter a  number: "))
C=float(input("Enter a number: "))
Average= (A+B+C)/3
print("The Average is ",Average)

#7.Calculate the area and perimeter of a right-angled triangle
Base= float(input("Enter the Base  of the Triangle: "))
Perpendicular_Height= float (input("Enter the height of the Triangle: "))
Hypotenuse= float(input("Enter the hypotenuse side of triangle: "))
Area = 1/2 * Base * Perpendicular_Height
Perimeter= Base + Perpendicular_Height + Hypotenuse
print("The Area of the Triangle is",Area)
print("The perimeter of the Triangle is",Perimeter)

#8. Create a program that asks the user to enter two numbers, then calculates and displays the results of addition, subtraction, multiplication, and division.
Num1=float(input("Enter a first number: "))
Num2=float(input("Enter a second number: "))
Addition = Num1 + Num2
Subtraction = Num1 - Num2
Multiplication = Num1 * Num2
if Num2 != 0:
    Division =  Num1 / Num2
else:
    Division = "undefined"

print("Addition: ",Addition)
print("Subtraction: ",Subtraction)
print("Multiplication: ",Multiplication)
print("Division: ",Division)
