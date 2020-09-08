'''
Prompts the user to enter a number in a while loop.
 gradually building up a list of he numbers entered.
When the user has finished, by pressing enter, print out:
- the numbers they entered
- The count of numbers
- The sum of the numbers
- The lowest
- The highest
- mean of the numbers (sum/count)
4 lines to initialize the necessary variables
less than 15 lines for the while loop including errors handling
25 lines max
'''

numbers = []
somma = 0
lowest = None
highest = None

while True:
	try:
		keyboard = input("Enter a number or Enter to finish: ")
		if not keyboard:
			break
		number = int(keyboard)
		numbers.append(number)
		somma += number
		lowest = min(numbers)
		highest = max(numbers)
		mean = somma/len(numbers)
	except ValueError as err:
		print(err)
	
print("Numbers:", numbers, "\nCount:", len(numbers), "\nSum:", somma, "\nLowest:", lowest, "\nHighest:", highest, "\nMean:", mean)