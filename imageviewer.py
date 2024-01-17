from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Image Viewer")

photo=ImageTk.PhotoImage(Image.open("homeicon.png"))
root.iconphoto(False, photo)

my_img1=ImageTk.PhotoImage(Image.open("viewer_img/cutedogs.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("viewer_img/cuddles.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("viewer_img/kawaii.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("viewer_img/koala.jpg"))
my_img5=ImageTk.PhotoImage(Image.open("viewer_img/teddy.jpg"))

#we create a list bcoz one of the easy ways to scroll through/access things is a list
my_list=[my_img1, my_img2, my_img3, my_img4, my_img5]
#it is easy to call/access any element of list with the help of indexing.
my_label=Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label    #we use global wnv we wanna use a variable outside of the particular func
    global b_forward
    global b_back
    my_label.grid_forget()    #internal grid function that is used to delete something// basically we want to delete/get rid of the first pic and then call the second pic after that so that they don't overlap
    my_label=Label(image=my_list[image_number])  #since we've entered 1 as img num, it'll display the first indexed img in list.
    my_label.grid(row=0, column=0, columnspan=3)
    b_forward=Button(root, text=">>", padx=3, pady=3, command=lambda:forward(image_number + 1))         #here, we updated the attribute to 2, so now frwd button value=2 until the forward button is clicked again
    if image_number==4:
        b_forward=Button(root, text=">>", padx=3, pady=3, state= DISABLED)

    b_forward.grid(row=1, column=2)
    b_back=Button(root, text="<<", padx=3, pady=3, command=lambda:back(image_number - 1))        #this assigns the back button value to 0
    b_back.grid(row=1, column=0)


def back(image_number):
    global my_label
    global b_forward
    global b_back
    my_label.grid_forget()
    my_label=Label(image=my_list[image_number])     #we can't consider back button from the 0 index img so we consider it from 1 index ==> the current img index is 1 and value of forward button is 2 & back button is 0
    #so when back is clicked, it takes you to index 0 img... 
    my_label.grid(row=0, column=0, columnspan=3)
    b_forward=Button(root, text=">>", padx=3, pady=3, command=lambda:forward(image_number +1))
    b_forward.grid(row=1, column=2)
    b_back=Button(root, text="<<", padx=3, pady=3, command=lambda:back(image_number - 1))
    if image_number==0:
        b_back=Button(root, text="<<", padx=3, pady=3, state=DISABLED)
    b_back.grid(row=1, column=0)


b_forward=Button(root, text=">>", padx=3, pady=3, command=lambda:forward(1))      #we type in '1' bcoz the next img that we navigate to is actually indexed as 1 in the list
b_forward.grid(row=1, column=2)

b_back=Button(root, text="<<", padx=3, pady=3, command=back, state=DISABLED)  #for back, we don't pass anything as when the program opens it already opens the first img so there's nothing to be 'back' navigated to.
b_back.grid(row=1, column=0)

b_exit=Button(root, text="Exit Program", padx=10, pady=3, command=root.quit)
b_exit.grid(row=1, column=1)


root.mainloop()


#let's try to understand by taking pic 3(index number 2) as refernce:
#So in the start, back=disabled... so it leaves us with the option to move forward only. Then, for moving forward we've given the forward button value as 1 initially (as seen in program)
#So after we move forward and come to the page where img index=1, our forward button number becomes 2 and back button number becomes 0.
#And then we click forward again-- so 2 becomes our new 'image_number' and we see my_img3 on output screen and our forward button is now 3 and back button becomes 1
# (evn though we've typed in value=1 when defining the b_forward outside def area... its value keep getting updated wnv the def func part is run,i.e., wnv we click the frwd button)
# so now, if we click the back button (who's attribute 'image_number' is 1 currently), it'll display the index 1 image(i.e., my_img2) on screen. So then the new/updated values of frwd button and back button are 2 and 0 respectively.
#since the values of both the buttons keep changing whn we go frwd or back, we need to specify both the values in the 'def func' area and so we use the gloabl variables. 



# Lambda func ==> They allow us to send multiple data through the callback function.