############################################################################################################################
##                                                Notes                                                                   ##
############################################################################################################################
#
# code hello.py <-- create hello.py within current open directory. save to see it in your explorer
# pwd <-- see current file path
# cd .. <-- go up in file path
# ls <-- see files/folders in current directory
# cd <file/folder> <-- go to file or folder underneath
# python hello.py <-- run the hello.py file with the python interpretter
# function - action or verb that lets you do something in a program
# method - built-in function
# argument - input to a function that influences its behavior
# side effects - the effect of a program "hello, world" being printed
# bug - a mistake in a program 
# return values - output from a program 
# variables - a container that stores a value inside a program or a value
# "=" is an assignment and not signifying equality
# comments - notes to yourself in your code
# pseudocode - using comments and english to express your thoughts
# in programming, there are many ways to solve the same problem.
# you can pass multipule arguments into functions
# string - sequence of text
# parameters - a value passed into a function
# if you want to use quotes inside a print, use different quotes on the inside and outside
# program will print exactly what your user inputs.
# this can be cleaned by adding .strip() <- removes whitespace from around the string
# press the up arrow when in the terminal to see past commands 
# 
############################################################################################################################
# 59:22

# ask the user for their name 
name = input("what's your name? ")

# remove the whitespace from the string
# name = name.strip()

# capitalize user's first name
# name = name.capitalize()

# make user's name title case
# name = name.title()

# chain the methods together to clean up the code
# strip and title case 
# could also add that to the original name assignment
name = name.strip().title()

# split user's name into first name and last name
first, last = name.split(" ")


# say hello to the user 
print(f"Hello, {first}.") 