"""Example memory diagram program"""

age: int = int(input("What is your age? "))
year: int = int(input("What year is it? "))
age_in_2041: int = 2041 - year + age
print("Your age in 2041 will be " + str(age_in_2041))

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))

