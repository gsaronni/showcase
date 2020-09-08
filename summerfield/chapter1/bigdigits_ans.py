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
import sys

zero = ["  ***  "," *   * ","*     *","*     *","*     *"," *   * ","  ***  "]
one = ["   * "," * * ","*  * ","   * ","   * ","   * ","  ***"]
two = [" *** ","*   *","*  * ","  *  ","*    ","*    ","*****"]
three = [" *** ","*   *","    *","   **","    *","*   *"," *** "]
four = ["   * ","  ** "," * * ","*  * ","*****","   * ","   * "]
five = ["*****","*    ","*    "," *** ","    *","    *"," *** "]
six = [" *** ","*    ","*    "," *** ","*   *","*   *"," *** "]
seven = ["*****","    *","    *","   * ","  *  "," *   ","*    "]
eight = [" *** ","*   *","*   *"," *** ","*   *","*   *"," *** "]
nine = [" *** ","*   *","*   *"," *** ","    *","    *"," *** "]

Digits = [zero, one, two, three, four, five, six, seven, eight, nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for f in digit[row]:
                if f == "*":
                    f = str(number)
                line += f
            line += "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("please enter a base ten number")
except ValueError as err:
    print(err, "in", digits)