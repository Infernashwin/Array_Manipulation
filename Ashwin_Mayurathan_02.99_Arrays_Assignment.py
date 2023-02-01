#Name: Ashwin_Mayurathan_02.99_Arrays_Assignment.py
#Programmer: Ashwin Mayurathan
#Date: October 5th, 2020
#Description: This code takes in integers and operators, and allows the user
#             to input mini lists sizes. The code will output the numbers
#             inputed, operators inputed, a list of operators used, 3 mini lists
#             of the user's choice of size, the sum of all odd, even, and all
#             integers inputed, and finally the value of the expression that
#             the user had inputted.

# Initialize Variables

input_loop = True # determines when the "input loop" should start/stop
numbers_list = [] # stores the integers
operator_list = [] # stores the operators in the order given
operators_count = [0,0,0,0] # counts how many times an operator is used
operators_used = [] # stores an operators if it is used
mini_list_size = 0 # determines size of the mini lists
middle_portion = [0,0] # stores the start and end point of the middle mini list
odd_total = 0 # represents the total of all odd intergers added
even_total = 0 # represents the total of all even intergers added
addition_total = 0 # represents the total of all intergers added
expression_total = 0 # represents the total when we evaluate the expression

# Start of Input Statements

# Allows user to input the intergers and operators in the "input loop"
# Uses the .isdigit() function (learned in the string document) to check if
# the input is an integer or an operator. The line "program_input[1:].isdigit()"
# is required to support negative integers, as the "-" makes .isdigit return
# False.
while input_loop:
    program_input = input()
    if program_input[1:].isdigit() or program_input.isdigit():
        numbers_list.append(int(program_input))
        
    else: # The else here is for when the input is an operator
        
        if program_input == "+": # What should happen if we input a +
            operators_count[0] += 1 # Stores the number of times + is inputted
            operator_list.append(program_input)

        elif program_input == "-": # What should happen if we input a -
            operators_count[1] += 1 # Stores the number of times - is inputted
            operator_list.append(program_input)

        elif program_input == "*": # What should happen if we input a *
            operators_count[2] += 1 # Stores the number of times * is inputted
            operator_list.append(program_input)

        elif program_input == "/": # What should happen if we input a /
            operators_count[3] += 1 # Stores the number of times / is inputted
            operator_list.append(program_input)

        elif program_input == "=": # What should happen if we input a =
            input_loop = False #Ends the "input loop"

        else: # What should happen if we input is invalid
            print("The last input was invalid")

# Allows user to input their desired mini list size
mini_list_size = int(input("What is the mini list size "))

#End of Input Statements

#Start of Processing Statements

# Checks if operators were used, and if so adds it to a list recording the
# operators used. Done by recording the count of how many times said operator
# was used. Index 0 is addition, 1 is substraction, 2 is multiplication and
# 3 is division.
if operators_count[0] > 0:
    operators_used.append("+")
    
if operators_count[1] > 0:
    operators_used.append("-")
    
if operators_count[2] > 0:
    operators_used.append("*")
    
if operators_count[3] > 0:
    operators_used.append("/")
    
# Defines the middle list size
middle_portion[0] = (len(numbers_list)-mini_list_size)//2 # start of middle 
                                                          # mini list
middle_portion[1] = middle_portion[0] + mini_list_size    # end of middle
                                                          # mini list

# Checks if mini list size is bigger than the actual list size, and if so
# resets the middle portion so it is the entire list
if mini_list_size >= len(numbers_list):
    middle_portion[0] = 0
    middle_portion[1] = len(numbers_list)

# Adds the total of all numbers, the even numbers and the odd numbers and
# stores them in variables
for elem in numbers_list:
    if elem%2 != 0:
        odd_total += elem
    else:
        even_total += elem
    addition_total += elem

# Checks if there is any numbers, since if there is not the loop will not work
if len(numbers_list) == 0:
    expression_total = 0

# A loop to do the expression given in the "input loop"
else:
    expression_total = numbers_list[0] # Starts by setting the total as the
                                       # first integer inputed
    for i in range (len(operator_list)):
        if operator_list[i] == "+":
            expression_total += numbers_list[i+1]
        elif operator_list[i] == "-":
            expression_total -= numbers_list[i+1]
        elif operator_list[i] == "*":
            expression_total *= numbers_list[i+1]
        else:
            expression_total /= numbers_list[i+1]

# End of Processing Statements

# Start of Output Statements
            
print (numbers_list) # The numbers that were inputed
print (operator_list) # Operators in the order given
print (operators_used) # Operators that were used
print(numbers_list[:mini_list_size]) # Front Mini List
print(numbers_list[-1*(mini_list_size):]) # Back Mini List
print(numbers_list[middle_portion[0]:middle_portion[1]]) # Middle Mini List  
print("Sum of even integers:",even_total) # Sum of all even integers
print("Sum of odd integers:",odd_total) # Sum of all odd integers
print("Sum of all integers:",addition_total) # Sum of all integers
print("Expression evaluates to:",expression_total) # Expression solution

# End of Output Statements
