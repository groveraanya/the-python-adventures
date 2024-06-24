'''
This program converts a list of integers into an actual integer.
The 'HOW THIS WORKS' is outlined below:
(1) The user inputs a list of integers as a string.
(2) The list is processed so that only the numerical characters (as string) are left.
(3) The numerical characters are converted into integers and deposited into a new list.
(4) The list of integers are combined into a single integer by treating it as a whole number.
(5) The output is a single integer.
The 'WHY IT WORKS' is outlined below:
By shifting each integer appropriately (with decreasing powers of 10) and adding them all together, we use the input-ted integers as building blocks to make the larger whole integer.
This is a mimic to one reading a sequence of digits from left to right and viewing it as a larger number with all the digits in it.
'''

# this is only used to get rid of the decimal place.
from math import trunc

# getting a list as a string from the user and converting it into a list
user_input = list(input('Please enter a list of integers (For example: [1,2,3,4]):\n>>> '))

# To remove the unwanted elements from the list that are not part of the actual number.
for element in user_input:
  if element.isdigit() == False:
    user_input.remove(element)

   
# Intialising the empty list for storing the integers after converting the string elements to integers.
int_list = []

# To iterate through the list of strings and convert each element into an integer and then store it in the list intialised for integers.
for string_element in user_input:
	int_list.append(int(string_element))

# initialising the variable to store the number.
whole_num = 0

# used to keep track of the place value for each digit.
# the original value is kept at the largest place value and is used for "shifting" the left-most digit
# this value decreases by a factor of 10 for each subsequent digit.
shifting = 10 ** (len(int_list) - 1)

for integer in int_list:
	whole_num += integer * shifting
	shifting = shifting / 10
	if shifting == 0:
		break

# Using the trunc method to get rid of the decimal places that were obtained after the algorithm.
whole_int = trunc(whole_num)

# Outputs the integer.
print('Here is your integer:', whole_int)
