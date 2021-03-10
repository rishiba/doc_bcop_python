# Any line starting with # is called a comment. This is used to document the code.
# This makes life easier for people who read your code. Also it enables you to
# understand your code faster if you are reffering to it after a long time.

# variables can have any names

x = 10
y = 20
z = 30
anyVariableName = 30

# Here x, y, z, anyVariableName are variable names

# Variables can be printed using print() function.

print("value of x is ", x)
print("value of y is ", y)
print("value of z is ", z)
print("value of anyVariableName is ", anyVariableName)

# You can print all the values using a single print statement

print("x = ", x, " y = ", y, " z = ", z, "anyVariableName = ", anyVariableName)

# Variables can store the values of the other variables.
print("value of x before is ", x)

x = y

print("Changed value of x after writing is ", x)

# Add two variables and store in third

x = y + z

print("x is ", x)

# Add self value to self
# Read this as "take the value of x and add to value of x, save the result into x"

print("x before operation", x)
x = x + x
print("x after operation", x)

#
# Till now we were just learning concepts. Let's do some useful work.
# We will now use variables to do some work. Also - currently do not worry about
# inputing a value from the user. That is a small work once you understand some
# basic concepts.
#
# For example calculating profit.
#

profitPercentage = 10
costPrice = 100

# BODMAS rule apply. Use brackets for complex work. Be safe.
profit = costPrice * (profitPercentage / 100)

# Python statements can go to next line as well. This is a good programmig
# practice so that the code looks a bit structured. Make a note of it so that
# incase you get this somewhere, you are not surprised.

print("Profit for profitPercentage as ", profitPercentage,
      " and costPrice as ", costPrice, " is profit ", profit)

# Another way of doing it. Here we are writing the formula inside the print statement.
# This is not advised. Do not do this.

print("Profit for profitPercentage as ", profitPercentage,
      " and costPrice as ", costPrice, " is profit ",
      costPrice * (profitPercentage / 100))

# Let us use the operators and variables to find the digits of a 5 digit number.
# This is one of the questions in your assignments.

fiveDigitNumber = 12345

firstDigit = fiveDigitNumber % 10

fiveDigitNumber = fiveDigitNumber / 10

secondDigit = fiveDigitNumber % 10

fiveDigitNumber = fiveDigitNumber / 10

thirdDigit = fiveDigitNumber % 10
fiveDigitNumber = fiveDigitNumber / 10
fourthDigit = fiveDigitNumber % 10
fiveDigitNumber = fiveDigitNumber / 10
fifthDigit = fiveDigitNumber

# Just print the digits here

print("First Digit is ", firstDigit)
print("Second Digit is ", secondDigit)
print("Third digit is ", thirdDigit)
print("Fourth digit is ", fourthDigit)
print("Fifth digit is", fifthDigit)

# Now finding the sum of all digit is pretty simple.

sumOfAllDigits = firstDigit + secondDigit + thirdDigit + fourthDigit + fifthDigit

print("Sum of all digits is ", sumOfAllDigits)

# Now, try finding out average, multiplication for all the above digits.

# Use the above concept to solve the problems in the assignments.
# Understand the above concept properly. This is simple number system.
