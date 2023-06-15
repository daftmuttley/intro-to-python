# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
name = input("What's your name? ")

if name == "Bob":
    print("Hello Bob")

# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".

# name = input("What's your name? ")

# if name == "Alice":
#     print("Hello Alice")

# else:
#     print("You're not Alice")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".

# password = input("Please enter a password ")

# if password == "qwerty123":
#     print("You have successfully logged in")


# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".

# number = int(input("Please enter a number "))

# if (number % 2) == 0:
#     print("Even")

# else:
#     print("Odd")


# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"

# num1 = int(input("PLease enter the first number "))
# num2 = int(input("Please enter the second number "))

# if ((num1+num2) > 21):
#     print("Bust")
# else:
#     print("Safe")
  
# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.

# len = int(input("Please enter the length "))
# wid = int(input("Please enter the width "))

# if (len == wid):
#     print("It's a square")
# else:
#     print("It's not a square")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

# salary = int(input("Please enter your salary\n "))
# length = int(input("How many years have you worked here?\n "))
# bonus = 0.1*salary

# if length > 3:
#     print("You will receive your salary of " + str(salary) + " and a bonus of " + str(bonus))
# else:
#     print("No bonus!")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.




# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".

# name = input("Please enter you name\n")

# if name == "Alice":
#   print("Hello, Alice")
# elif name == "Bob":
#   print("You're not Bob, I'm Bob!")
# else:
#   print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"

age = int(input("Please enter your age\n"))

if age < 11:
  print("You're too young to go to this school")
elif age <= 16:
  print("You can can come to this school")
elif age == 0:
  print("You're not born yet!")
elif age > 16:
  print("You're too old for school")


# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".

# month = input("Please enter a month\n")

# if month == "March" or month == "May" or month == "June":
#   print(month + " is in Spring")
# elif month == "July" or month == "August":
#   print (month + " is in Summer")
# elif month == "September" or month == "October" or month == "November":
#   print (month + " is in Autumn")
# elif month == "December" or month == "January" or month == "February":
#   print (month + " is in Winter")
# else:
#   print ("I don't know")

# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.

# num1 = int(input("Please enter the first number\n"))
# num2 = int(input("Please enter a second number\n"))

# if (num1 % 2) == 0 and (num2 % 2) == 0:
#   print ("Even")
# elif (num1 % 2) == 1 and (num2 % 2) == 1:
#   print("Odd")
# else:
#   print(num1 * num2)

# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.

# num1 = int(input("Please enter the first number\n"))
# num2 = int(input("Please enter a second number\n"))

# if num1 > num2:
#   print (num1)

# else:
#   print (num2)

# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.

salary = int(input("Please enter your salary\n "))
length = int(input("How many years have you worked here?\n "))


if length > 7:
  print("You will receive your salary of " + str(salary) + " and a bonus of " + str(0.2 * salary))
elif length > 5:
  print("You will receive your salary of " + str(salary) + " and a bonus of " + str(0.15 * salary))
elif length > 3:
  print("You will receive your salary of " + str(salary) + " and a bonus of " + str(0.1 * salary))
else:
  print("No bonus!")

# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.



# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
