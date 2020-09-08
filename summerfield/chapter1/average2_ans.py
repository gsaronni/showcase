'''
Copyright 2010 Pearson Education, Inc.
This program is free software:
you can redistribute it and/or modify it under the terms of the GNU General
 Public License as published by the Free Software Foundation,
 either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
GNU General Public License for more details.

You should have received a copy of the GNU General Public License 
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''
numbers = []
somma = 0
lowest = None
highest = None
median = None
count = 0

while True:
	try:
		keyboard = input("Enter a number or Enter to finish: ")
		if not keyboard:
			break
		number = int(keyboard)
		numbers.append(number)
		count += 1
		somma += number
		lowest = min(numbers)
		highest = max(numbers)
		mean = somma/len(numbers)
	except ValueError as err:
		print(err)

if count % 2 == 0:
	print("Numbers:", numbers, "\nCount:", len(numbers), "\nSum:", somma, "\nLowest:", lowest, "\nHighest:", highest, "\nMean:", mean)
	
else:
	median = (count / 2) + 0.5
	middle = numbers[int(median - 1)]
	print("Numbers:", numbers, "\nCount:", len(numbers), "\nSum:", somma, "\nLowest:", lowest, "\nHighest:", highest, "\nMean:", mean, "\nMedian:", middle)

'''
check if the list of number is even
if is even
	put the lowest number at the lowest index
switch index by an inch and do it again until last number
'''

	

#Calculate Median and Mean
#Median is obtained sorting the list and getting the middle number if the list has an odd number of items