# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
# length = 4
# width = 3
# area = length * width
# print("Area = " + str(area))

# 2. Write code that prints the length of the string, 'python'.

# name = "python"
# name_length = len(name)

# print("The length of the word python is " + str(name_length))
# 3. Print out the first and third letter of the word 'python'.

# print("The first and third letters of " + str(name) + " are " + str(name[0]) + " and " + str(name[2]))

# 4. Ask the user to enter their name, and print out `Hello, <name>`.

# name = input ("What is your name?")

# print("Hello " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
# age = int(input("What is your age?"))
# age_in_15_years = age + 15

# print("You will be " + str(age_in_15_years) + " in 15 years time")
# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.

# print("Hello " + str(name) + ", in 15 years time you will be " + str(age_in_15_years))

# 7. Ask the user to enter their hometown, print it out in uppercase letters.

# hometown = input("What is your hometown?")

# print(hometown.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.

# favourite_colour = input("What is your favourite colour?")
# colour_length = len(favourite_colour)

# print("The length of your favourite colour is " + str(colour_length))

# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.

# weather = input("What is the weather today?")
# month = input("What is the current month?")

# print("It is " + str(month) + " and it is " + str(weather))

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.

# month = input("What is the month? ")
# value1 = input ("Enter a temperature ")
# value2 = input("Enter another temperature ")
# value3 = input("Enter a 3rd temperature ")
# value4 = input("Enter a 4th temperature ")
# value5 = input("Enter a final temperature ")

# average =(int(value1) + int(value2) + int(value3) + int(value4) + int(value5))/5

# print("It is " + str(month) + " and the average temperature is " + str(average) + " degrees celsius")

# 11. Print out the above sentence but make the month upper case.

# print("It is " + str(month.upper()) + " and the average temperature is " + str(average) + " degrees celsius")

# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.



# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.

# name = input("What is your name? ")
# number = int(input("Please enter a number "))

# print(name[number].upper())


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
# str = "WelcometoPython"
# length = len(str)
# print(length)
# print(str[1:14:2])
