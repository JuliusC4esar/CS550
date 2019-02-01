from tkinter import *
import sys

# Kai 
# On my honor, I have neither given nor received unauthorised aid.
# Sources: http://effbot.org/tkinterbook/
# Sources: https://www.youtube.com/watch?v=a1Y5e-aGPQ4&t=6s
# Sources: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y

# Extremely basic code examples for the iBook, which covers the fundamentals of Tkinter.


# Example of basic UI. Log in functionality. Password is helloworld
root = Tk() # Create the master window called "root"

root.geometry('500x500') # Set window size using one of the many functions in the Tk() class

def LogIn():

	txt = entryfield.get() # Get() function from Entry class, discovered in Tkinter documentation

	if txt == "helloworld": # If the input text is equal to a password

		accessgranted = Label(text="Access Granted",fg="green",font=("times",30)).place(relx=0.5,rely=0.7) # Create a green label that says "Access Granted"

root.configure(background="white",cursor="pirate") # Set background to white and set a custom cursor 

entryfield = Entry() # Create entry field

entryfield.place(relx=0.5,rely=0.5,width=100,height=50) # Place entry field

button = Button(text="Log In",command=LogIn).place(rely=0.5,relx=0.7,width=50,height=50) # Create and place button

root.mainloop() # MAIN LOOP






# Example of custom StringVar class being used, as well as button and label instantiation. Enter something into the text box and push the button to print the inputted text.
root = Tk() # Create the window

def buttonfunction(): # Button Function

	print(var.get()) # Get the StringVar value and print it

myButton = Button(root,text="This is a button.",command=buttonfunction).place(x=10,y=10,width=100,height=100) # Create button for above function

var = StringVar() # Define the StringVar

entry = Entry(root,textvariable=var,cursor="box_spiral",justify=CENTER).place(x=10,y=110,width=100,height=25) # Reference the StringVar in the input field

# Example of label parameters
label = Label(root,text="This is a label.",fg="blue",bg="red").place(x=120,y=10,width=200,height=20)

root.mainloop() # MAIN LOOP






root = Tk() # Example of Place Geometry Manager

label = Label(text="hi")

label.place(x=100,y=100)

root.mainloop()






root = Tk() # Example of Grid Geometry Manager

label = Label(text="hi").grid(row=0,column=0)

label2 = Label(text="hi").grid(row=1,column=0)

label3 = Label(text="hi").grid(row=0,column=1)

label4 = Label(text="hi").grid(row=1,column=1)



# Example of Pack Geometry Manager
window = Toplevel(root) # Create new window called "Window"

label = Label(window,text="hi").pack(side=LEFT,padx=100) # Pack two labels on the left of the screen, total of 200 pixels away from each other.

label2 = Label(window,text="hi2").pack(side=LEFT,padx=100)


root.mainloop() # Mandatory loop



root = Tk() # Create Tk() class

root.title("This is a window.")  # One of the many Tk() functions
 
root.geometry('500x500') # One of the many Tk() functions

root.configure(background="blue") # One of the many Tk() configurations

root.mainloop()


root = Tk() # Make the Tk() class

root.configure(background="black") # black background

button = Button(root,text="This is a button.") # Button Instantiation

button.place(relx=0.5,rely=0.5) # Place button 1/2 of the way to the right, 1/2 of the way down.

root.mainloop()













