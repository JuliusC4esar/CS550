# Kai 
# On my honor, I have neither given nor received unauthorised aid.
# Sources: http://effbot.org/tkinterbook/
# Sources: https://www.youtube.com/watch?v=a1Y5e-aGPQ4&t=6s
# Sources: https://www.youtube.com/watch?v=RJB1Ek2Ko_Y
# Description: Basic UI with a login functionality. Clearly shows a variety of Tkinter functions and tools. Password is carrot88
from tkinter import *
from tkinter import ttk
from PIL import Image # For images
from PIL import ImageTk


root = Tk() # Create the main window class


# Image of Athena
athenaload = Image.open("athena.png") # Load image of Athena
athenaimage = ImageTk.PhotoImage(athenaload) # Instantiate image of Athena into variable
athenashow = Label(root,image=athenaimage) # Load image of Athena into Label class
athenashow.image = athenaimage


# Functionality of Quit button in GUI
def exit():
	root.destroy()



# Functionality of Log In button in GUI
def LogIn():

	if str(entry.get()) == password: # Check if entry field text is equal to password

		access.place_forget() # Remove access denied label

		granted() # Initiate function for access granted

	else:

		# Place Access Denied label
		access.configure(text="")
		access.configure(text="Access Denied.",fg="red")
		access.place(relx=0.31,rely=0.83)




password = "carrot88" 


# Instantiate Quit button
quitbutton = Button(root,command=exit,bg="black",fg="black",text="Quit Console",font=("times",30),cursor="circle")
quitbutton.place(relx=0.8,rely=0.9)

# Instantiate Welcome text
welcome = Label(root,text="Welcome, agent. I am Athena. Please verify your identity before proceeding.",font=("times",23),fg="white",bg="black")
welcome.place(x=15,y=35)


# Instantiate Access Denied Label, but text is not yet set
access = Label(text="",bg="black",font=("times",40))


# Set the configurations of the root window
root.configure(background = "black")
root.geometry('900x700')
root.title("This is my window!")

# Instaniate the input field for password input
entry = Entry(root,justify=CENTER)
entry.place(relx=0.3,rely=0.7,width=300,height=50)

# Instantiate the Log In Button
loginbutton = Button(root,text="Log In",command=LogIn,font=("times",20),cursor="box_spiral")
loginbutton.place(relx=0.7,rely=0.7,height=50,width=150)

# Show the image of Athena
athenashow.place(rely=0.2,relx=0.3,width=300,height=300)


# Image of Omnics
title = Label(text="The Omnics",bg="blue",fg="red",font=("times",50))
imageload = Image.open("omnics.jpg")
theimage = ImageTk.PhotoImage(imageload)
imagelabel = Label(root,image=theimage)
imagelabel.image = theimage


# Image of Humans
title1 = Label(text="The Humans",bg="blue",fg="black",font=("times",50))
imageload1 = Image.open("overwatch.png")
theimage1 = ImageTk.PhotoImage(imageload1)
imagelabel1 = Label(root,image=theimage1)
imagelabel1.image = theimage1

# List of checkboxes
checkboxes = []

# Add checkbuttons of different contents to checkboxes list
for i in ["Destroy Omnics","Steal Intelligence","Engage in Tactful Political Negotiations","Conduct Air Raid","Disarm Omnic Offensive Mechanisms","Be Cool","Update Security System","Feed Winston"]:

	checkboxes.append(Checkbutton(root,text=i,font=("times",18),bg="blue",fg="orange",cursor="pirate"))


def morewidgets(): # Show the checkbox list checkbuttons. Line them up vertically.

	for i in range(8):

		checkboxes[i].place(rely=(0.45+(0.05*i)),relx=0.4)



def omnicdescription(): # Show the image and text of the omnics 

	title.place(rely=0.1,relx=0.1)

	imagelabel.place(rely=0.2,relx=0.05,width=300,height=150)


def humandescription(): # Show the image and text of the humans 

	title1.place(rely=0.1,relx=0.6)

	imagelabel1.place(rely=0.2,relx=0.6,width=300,height=170)



def loggedout(): # Function to be executed when logged out 

	quitbutton.place(relx=0.8,rely=0.9) # Show the Quit button

	welcome.configure(text="Welcome, agent. I am Athena. Please verify your identity before proceeding.",font=("times",23),fg="white",bg="black") # Show the welcome text

	root.configure(background = "black") # Revert background color

	entry.place(relx=0.3,rely=0.7,width=300,height=50) # Place the password entry field

	loginbutton.configure(command=LogIn,text="Log In") # Revert the log in button
	loginbutton.place(relx=0.7,rely=0.7,height=50,width=150)


	# Remove images and text of Omnics and Humans, restore Athena image.
	title.place_forget()
	title1.place_forget()
	imagelabel.place_forget()
	imagelabel1.place_forget()
	athenashow.place(rely=0.2,relx=0.3,width=300,height=300)


	# Remove checkbuttons
	for i in range(8):

		checkboxes[i].place_forget()


def granted(): # When logged in

	athenashow.place_forget() # Remove Athena image

	root.configure(background = "blue") # Change background color

	welcome.configure(text="Access Granted. Welcome, Soldier 76. Preparing classified to-do list...",bg="blue",fg="white") # Change welcome text

	entry.place_forget() # Remove password entry field

	loginbutton.configure(command=loggedout,text="Log Out") # Change login button to logout button

	loginbutton.place(relx=0.8,rely=0.9) # Set logout button position

	quitbutton.place_forget() # Remove Quit button


	# Show Omnic and Human images and text, show the checkbuttons list.
	omnicdescription()
	humandescription()
	morewidgets()


root.mainloop() # Required main loop



	






