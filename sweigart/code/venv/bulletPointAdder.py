#! python3
# bulletPointAdder.py - Adds WIkipeia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)):   # lopp through all indexes in the "lines" list
  lines[i] = '* ' + lines[i]  # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
