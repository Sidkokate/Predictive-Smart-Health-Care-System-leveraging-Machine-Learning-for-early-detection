
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk


##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Disease Prediction System")



# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('bg2.jpg')
image2 = image2.resize((900,600), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=350, y=60)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text=" DISEASE PREDICTION SYSTEM",font=("Times New Roman", 35, 'bold'),
                    background="white", fg="black", width=55, height=2)
label_l1.place(x=0, y=0)



def reg():
    from subprocess import call
    call(["python","register.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=12, height=2,bd=5,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=400, y=400)

button2 = tk.Button(root, text="Register",command=reg,width=12, height=2,bd=5,font=('times', 20, ' bold '), bg="#152238", fg="white")
button2.place(x=700, y=400)

button2 = tk.Button(root, text="EXIT",command=window,width=12, height=2,bd=5,font=('times', 20, ' bold '), bg="red", fg="white")
button2.place(x=1000, y=400)


root.mainloop()