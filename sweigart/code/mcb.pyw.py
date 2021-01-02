# .pyw extension won't show a terminal window when runs

'''
Create a batch file to run it from windows

@pyw.exe C:\Python34\mcb.pyw %*

Usage:
py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
py.exe mcb.pyw <keyword> - Loads keyword to clipboard
py.exe mcb.pyw list - Loads all keywords to clipboard
'''

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')

