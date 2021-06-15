# (1) Getting Started
# Example of a built-in function
# print("Hello")

# The input() function prompts the user for input
# input("What is your name? ")

# Example of using a Variable and the Print function
# myName = "Dany"
# print(myName)




# (2) Examples with Variables
# Ask the user for input
# userName = input("What is your name? ")

# Confirm their response
# print("You entered", userName)

# (3) Rules for naming Variables
# 1 - No special characters except for _
# 2 - Cannot begin with a number
# 3 - Always start with lowercase letter
# 4 - Do not name variables after reserved keywords
# 5 - Use camel case notation

# Adding line breaks with \n
# print("One line\nSecond line")




# (5.a) Solution to Exercise 1 (Option A)
# firstName = input("What is your first name? ")
# lastName = input("What is your last name? ")
# email = input("What is your email address? ")
# phoneNumber = input("What is your phone number? ")

# print("Thank you for registering. Here is what you entered.")
# print("Your first name:", firstName)
# print("Your last name:", lastName)
# print("Your email:", email)
# print("Your phone number:", phoneNumber)


# (5.b) Solution to Exercise 1 (Option B)
# firstName = input("What is your first name? ")
# lastName = input("What is your last name? ")
# email = input("What is your email address? ")
# phoneNumber = input("What is your phone number? ")

#print(firstName + "\n" + lastName + "\n" + email + "\n" + phoneNumber)




# (6) Data Types
# Strings
# Numbers
# Data Structures (Lists, Tuples, Sets, and Dictionaries)
# Classes and Objects

# Strings (letters, numbers, special characters)
# myName = "John"
# myFullName = 'John Doe'
# someSentence = "Today is a good day!"
# contactNumber = "00971 50 123 4567"
# sentenceWithEscapedCharacter = "She said \"Good Morning\" "

# Numbers (Integers, 32-Bit Float, 64-Bit Float)
# thePrice = 1000
# afterDiscount = 900.5
# print(thePrice + afterDiscount)

# Enumeration (Lists, Tuples, Sets, Dictionaries)

# customerA = ['John','Doe','jon@gmail.com','050 1234567']
# customerB = ['Jane','Doe','jane@gmail.com','050 7654321']


# Examples with Lists
# Definition: Elements
# Elements have Keys and Values
# cities = [
#     'Abu Dhabi',    # 0
#     'London',       # 1
#     'Tokyo',        # 2
#     'Paris',        # 3
#     'Berlin'        # 4
# ]




# (7) Comparison Operators
# <                 Less than comparison
# >                 Greater than comparison
# <=                Less than or equal comparison
# >=                Greater than or equal comparison
# ==                Equality comparison
# !=                Not equal comparison
# ||                Or comparison
# &&                And comparison




# (8) Control Statements (if/else, while, for)

# Basic Example
# price = 500
# budget = 500

# if price <= budget:
#     print("Buy this product")
# else:
#     print("Don't buy this product")


# Example Multiple Conditions 

# iPhone 12, Note 20, P30
# 3700, 3600, 3300

# selectedProduct = "3310"

# if selectedProduct == "iPhone 12": 
#     print(3700)
# elif selectedProduct == "Note 20":
#     print(3600)
# elif selectedProduct == "P30":
#     print(3300)
# else:
#     print("Product not available")


# Solution to Exercise 2

# Latte, Americano, Cappuccino, Mocha, Espresso.
# 18, 13, 15, 30, 12


# selectedCoffee = input("Choose you preferred coffee. Enter a number between 1 to 5: ")

# if selectedCoffee == "1":
#     print("Latte", 18)
# elif selectedCoffee == "2":
#     print("Americano", 13)
# elif selectedCoffee == "3":
#     print("Cappuccino", 15)
# elif selectedCoffee == "4":
#     print("Mocha", 30)
# elif selectedCoffee == "5":
#     print("Espresso", 12)
# else:
#     print("Selection not recognized")


# For Loop

# coffeeOptions = [
#     'Latte',            
#     'Americano',
#     'Cappuccino', 
#     'Mocha',
#     'Espresso'
# ]

# for currentElement in coffeeOptions:
#     print('We have', currentElement)


# customers = [
#     'Vijayam',
#     'Warren',
#     'Bismah',
#     'Mohanad',
#     'Reem'
# ]

# for currentCustomer in customers:
#     print("Dear", currentCustomer, "We have a BIG sale...just for you")


# Example of using for loop and if statement.
# destinations = [
#     'dxb',
#     'jfk',
#     'lax',
#     'auh',
#     'iah'
# ]

# airport = input("Where do you want to fly to? ")

# if airport in destinations:
#     print("Yes, we fly there")
# else:
#     print("No :(")




# (9) List Methods
# .append() Adds items to the end of the list
# .pop() removes an element from the end of list or at specified position
# len() Count number of elements in the list

# coffeeOptions = [
#     'Latte',
#     'Americano',
#     'Espresso',
#     'Mocha'
# ]

# # Add a coffee type
# coffeeOptions.append("Cappuccino")

# # Remove a coffee type
# coffeeOptions.pop(2)

# # Count the length of the list
# sizeOfcoffeeOptions = len(coffeeOptions)
# print(sizeOfcoffeeOptions)


# Create the function
# def addTwoNumbers(numA, numB):
#     theSum = numA + numB
#     return theSum


# # Use the function
# print( addTwoNumbers(10, 5) )


# def coffeeMachine(coffeeType, sugar, size, milk):
#     theOrder = []

#     theOrder.append(coffeeType)
#     theOrder.append(sugar)
#     theOrder.append(size)
#     theOrder.append(milk)

#     return theOrder

# coffeeForRag = coffeeMachine("Americano", "brown sugar", "small", "no milk")
# coffeeForFeras = coffeeMachine("Frappacino", "honey", "large", "almond")
# coffeeForHubert = coffeeMachine("Espresso", "no sugar", "double", "no milk")


# print(coffeeForRag) 
# print(coffeeForFeras) 
# print(coffeeForHubert)




# (10) Examples with Lists, Sets, Tuples, and Dictionaries
# Example of List
# (1) Keys are ordered and numerical
# (2) Repeat values allowed
# List methods: https://www.w3schools.com/python/python_ref_list.asp
# cities = [
#     'Abu Dhabi', # 0 
#     'London',  # 1
#     'Tokyo', # 2
#     'Tokyo', # 3
#     'Tokyo', # 4
#     'Tokyo', # 5
# ]


# Example of Set
# (1) Unique elements
# (2) Order does not matter
# Set methods:
# https://www.w3schools.com/python/python_ref_set.asp
# countries = {
#     "United Arab Emirates",
#     "Japan",
#     "Germany",
#     "Australia"
# }

# Example of Tuple
# (1) Allows duplicates
# (2) Immutable
# Tuple methods: https://www.w3schools.com/python/python_ref_tuple.asp
# emirates = (
#     "Dubai",
#     "Sharjah",
#     "Abu Dhabi",
#     "Ajman",
#     "Ras Al Khaimah",
#     "Fujairah",
#     "Umm Al Quwain"
# )

# Example of Dictionary
# (1) Keys must be defined and unique
# (2) Mutable
# Dictionary methods: https://www.w3schools.com/python/python_ref_dictionary.asp
# airports = {
#     "dxb": "Dubai International Airport",
#     "jfk": "John F Kennedy Airport",
#     "auh": "Abu Dhabi International Airport",
#     "lax": "Los Angeles Airport"
# }

# airports['lax'] = 'Los Angeles Airport'




# (11) Examples with Mixed Data Structures
# moviesLibrary = {
#     "documentary": ["Earth with David Attenborough", "Top Gear"],
#     "horror": ["Insideous", "Ring", "The Conjuring"],
#     "comedy": ("Hangover 1", "Hangover 2", "Hangover 3"),
# }


# # Retrieve a specific movie
# moviesLibrary['documentary'][1]

# # Add a movie to the "horror" genre
# moviesLibrary['horror'].append("The Exorcist")

# # Add another genre to the list moviesLibrary
# moviesLibrary['sci-fi'] = ['E.T.', 'Gravity', 'Star Wars']

# allOfTheMovies = moviesLibrary.keys()
# print(allOfTheMovies)


# Solution to Exercise 2
# carShowroom = {}

# carShowroom['Tesla'] = ['Model S', 'Model E', 'Model X', 'Model Y']
# carShowroom['Toyota'] = ['Yaris Sedan', 'Corolla', 'Camry', 'Avalon']
# carShowroom['Merdedez Benz'] = ['A-Class Hatcback', 'A-Class Sedan', 'E-Class Sedan', 'S-Class Sedan']



# After adding models to the carShowroom
"""
carShowroom = {
    'Tesla': ['Model S', 'Model E', 'Model X', 'Model Y'], 
    'Toyota': ['Yaris Sedan', 'Corolla', 'Camry', 'Avalon'], 
    'Merdedez Benz': ['A-Class Hatcback', 'A-Class Sedan', 'E-Class Sedan', 'S-Class Sedan']
}
"""


# Acces the first car for Tesla
# carShowroom['Toyota'][1]



# Solution to Exercise 4
# def registerUser(firstName, lastName, email):
#     registrationDetails = []

#     registrationDetails.append(firstName)
#     registrationDetails.append(lastName)
#     registrationDetails.append(email)

#     return registrationDetails


# newUser = registerUser(
#     input("What is your first name? "),
#     input("What is your last name? "),
#     input("What is your email? ")
# )

# print(newUser)


# cities = ['Dubai','Abu Dhabi','Tokyo']
# tesla = ['Model S', 'Model E', 'Model X', 'Model Y']
# horrorMovies = ["Insideous", "Ring", "The Conjuring"]




# Declaring a Class
class Car:
    # Properties (variables in a Class)
    brand = ""
    noOfWheels = 0
    color = ""
    # Methods (functions in a Class)
    def __init__(self, brandArg, noOfWheelsArg, colorArg, engineArg):
        self.brand = brandArg
        self.noOfWheels = noOfWheelsArg
        self.color = colorArg
        self.engine = engineArg

    def accelerate(self):
        print(self.engine)

    def brake(self):
        print(self.engine)

# Instantiate
modelE = Car("Tesla", 4, "blue", "Musk10")
modelE.accelerate()


