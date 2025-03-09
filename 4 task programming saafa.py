#Create an application to determine whether a year is a leap year or not
Leap_year = int(input("Enter the year : "))
if (Leap_year % 4 == 0 and Leap_year % 100 != 0 or Leap_year % 400 == 0):
    print(Leap_year," is a leap year ")
else:
    print("Not a leap year")

#Create an application to determine the output: negative, positive, or zero.
number = float(input("Enter a number: "))
if number > 0 :
    print(number," is positive number")
elif number < 0 :
    print(number," is negative number")
else: 
    print(number," is zero")

#Create an application to calculate the total amount to be paid based on the year-end discount
total_purchase= float(input("Enter the amount: "))
if (total_purchase > 100000 ):
    discount= total_purchase* 10/100
elif (total_purchase >50000):
    discount= total_purchase * 5/100
else:
    discount= 0
total_amount = total_purchase - discount

print(f"Total  purchase is  ${total_purchase:,.2f}")
print (f"Discount amount is ${discount:,.2f}")
print (f"Total amount is ${total_amount:,.2f}")

#Give the scores for three subjects: Math, Science, and English. You will pass if you meet the following criteria
maths=float(input("Enter the maths marks: "))
science=float(input("Enter the science marks: "))
english= float(input("enter the english marks: "))
total_Score = maths + english + science
Average_score = total_Score/3
below_70 = sum(score < 70 for score in [maths,science,english])
if maths==100 or science==100 or english==100:
    print("pass(perfect score in one subject)")
elif Average_score > 75:
    print("pass)(average score > 75)")
elif below_70==1:
    print("pass(only one subject is below 70)")
else:
    print("fail")