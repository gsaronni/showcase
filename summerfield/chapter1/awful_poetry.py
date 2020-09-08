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
import random

articles = ('The', 'A')
subjects = ('Grognak', 'creature', 'alien', 'Gungan')
verbs = ('flew', 'hoped', 'slept', 'ran', 'vanished')
adverbs = ('quickly', 'carefully', 'loudly', 'patiently', 'politely')


for x in range(0,5):
	print(random.choice(articles), random.choice(subjects), random.choice(verbs), random.choice(adverbs))