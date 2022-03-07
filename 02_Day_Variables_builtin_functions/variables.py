# 'Day 2: 30 Days of python programming'


# Exercise: Level 1
"""
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line"""

first_name = "Cuong"
last_name = "Nguyen"
full_name = "Nguyen Cuong"
country = "Viet Nam"
city = "Ha Noi"
age = 16
year = 2022
is_married = False
is_true = True
is_light_on = False

first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = "Cuong", "Nguyen", "Nguyen Cuong", "Viet Nam", "Ha Noi", 16, 2022, False, True, False


# Exercise: Level 2
"""
- Check the data type of all your variables using type() built-in function
- Using the len() built-in function, find the length of your first name
- Compare the length of your first name and your last name
- Declare 5 as num_one and 4 as num_two
    + Add num_one and num_two and assign the value to a variable total
    + Subtract num_two from num_one and assign the value to a variable diff
    + Multiply num_two and num_one and assign the value to a variable product
    + Divide num_one by num_two and assign the value to a variable division
    + Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
    + Calculate num_one to the power of num_two and assign the value to a variable exp
    + Find floor division of num_one by num_two and assign the value to a variable floor_division
- The radius of a circle is 30 meters.
    + Calculate the area of a circle and assign the value to a variable name of area_of_circle
    + Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
    + Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
"""

#  Check the data type of all your variables using type() built-in function
print("Type of first_name variable:", type(first_name))
print("Type of last_name variable:", type(last_name))
print("Type of full_name variable:", type(full_name))
print("Type of country variable:", type(country))
print("Type of city variable:", type(city))
print("Type of age variable:", type(age))
print("Type of year variable:", type(year))
print("Type of is_married variable:", type(is_married))
print("Type of is_true variable:", type(is_true))
print("Type of is_light_on variable:", type(is_light_on))

print("------------------------------------------------")

# - Using the len() built-in function, find the length of your first name
# - Compare the length of your first name and your last name
print("Length of first_name:", len(first_name))
len_first_name = len(first_name)
len_last_name = len(last_name)
if len_first_name > len_last_name:
    print("len_first_name > len_last_name")
else:
    print("len_first_name < len_last_name")

print("------------------------------------------------")

# Declare 5 as num_one and 4 as num_two
nums_one = 5
nums_two = 4

sum_of_nums_one_nums_two = nums_one + nums_two
subtract = nums_one - nums_two
multiply = nums_one * nums_two
divide = nums_one / nums_two
remainder = nums_one % nums_two
exp = pow(nums_two, nums_one)
floor_division = nums_one // nums_two

# The radius of a circle is 30 meters.
radius_of_circle = 30
area_of_circle = pow(radius_of_circle,2) * 3.14
circum_of_circle = 2* 3.14* radius_of_circle



# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)