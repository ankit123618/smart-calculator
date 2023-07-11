import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("anku")
# Set the window size
window.geometry("400x300")

# Create a label widget
label = tk.Label(window, text="Hello, World!")

# Pack the label widget to display it
label.pack()

# Create a button widget
button = tk.Button(window, text="Click Me!")

# Pack the button widget
button.pack()

# Start the main event loop
window.mainloop()


#!/usr/bin/env python3
import sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.math import *
print(responses[0])
print(responses[1])
while True:
    print()
    text=input("enter your queries\n")
    for word in text.split(" "):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()] (l[0],l[1])
                print(r)
            except:
                print("something went wrong, please retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()] ()
            break
    else:
        sorry()


