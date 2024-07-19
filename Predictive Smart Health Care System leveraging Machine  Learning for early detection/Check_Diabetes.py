def Train():
    """GUI"""
    import tkinter as tk
    #from tkinter import ttk, LEFT, END
    from tkinter import messagebox as ms
    import sqlite3
    from PIL import Image, ImageTk
    import re

    ##############################################+=============================================================
    root = tk.Tk()
    root.configure(background="white")


    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0" % (w, h))
    root.title("Heart")


    # ++++++++++++++++++++++++++++++++++++++++++++
    #For background Image

    image2 = Image.open('dr4.jpg')
    image2 = image2.resize((w,h), Image.ANTIALIAS)

    background_image = ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=-10, y=0)  # , relwidth=1, relheight=1)



    label_l1 = tk.Label(root, text="Check Diabetes Disease",font=("Times New Roman", 30, 'bold'),
                        background="#131e3a", fg="white", width=67, height=1)
    label_l1.place(x=-60, y=0)
 
    
    Glucose=tk.IntVar()
    Blood_Pressure=tk.IntVar()
    Insulin=tk.IntVar()
    DiabetesPedigreeFunction=tk.IntVar()
    Age=tk.IntVar()
    
    #===================================================================================================================
       
    def window():
       root.destroy()
       from subprocess import call
       call(["python","main.py"])
    
    def Detect():
        e1=Glucose.get()
        e2=Blood_Pressure.get()
        e3=Insulin.get()
        e4=DiabetesPedigreeFunction.get()
        e5=Age.get()
        
        

        from joblib import dump , load
        a1=load("RF_MODEL.joblib")
        v= a1.predict([[e1,e2,e3,e4, e5]])
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Disease Detected",background="red",foreground="white",font=('times', 20, ' bold '),width=20)
            yes.place(x=700,y=150)
            
            label_l1 = tk.Label(root, text="LIST OF RECOMMENDED DOCTORS\n\n  1.Dr. Wadia (8181818181) \n\n  2.Dr. Sahara (8282828282)\n\n 3.Dr. Gupta (7878787878)\n\n 4.Dr. Khamkar (8585858585)",font=("Times New Roman", 22, 'bold'),
                                background="#152238", fg="white", width=30, height=10)
            label_l1.place(x=700, y=200)
            
            report_file = open(r"Report.txt","w")
            report_file.write("----Patient Report---- \nStatus : Diabetes Detected \n\n****Immidiately Visit Doctor For Consultation.****\n")
            report_file.close()
        else:
            print("No")
            no = tk.Label(root, text="No Disease Detected", background="green", foreground="white",font=('times', 20, ' bold '),width=20)
            no.place(x=700, y=150)
            report_file = open(r"Report.txt","w")
            report_file.write("----Patient Report---- \nStatus : No Diabetes Detected \n\n****")
            report_file.close()


    l1=tk.Label(root,text="Glucose",bd=0,background="#eff0f8",font=('times', 12, ' bold '),width=10)
    l1.place(x=110+400,y=200+100)
    Glucose=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 12),textvar=Glucose)
    Glucose.place(x=300+380,y=200+100)
    
    lbl = tk.Label(root, text="avg: 84 - 140"  , font=('times', 9), width=12,height=1,bg="#eff0f8",fg="grey")
    lbl.place(x=350+400, y=200+100)


    

    l3=tk.Label(root,text="Blood Pressure",background="#eff0f8",font=('times', 12, ' bold '),width=14)
    l3.place(x=110+400,y=240+100)
    Blood_Pressure=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 12),textvar=Blood_Pressure)
    Blood_Pressure.place(x=300+380,y=240+100)
    
    lbl = tk.Label(root, text="avg: 80 - 120"  , font=('times', 9), width=12,height=1,bg="#eff0f8",fg="grey")
    lbl.place(x=350+400, y=240+100)
    
    

    l4=tk.Label(root,text="Insulin",background="#eff0f8",font=('times', 12, ' bold '),width=14)
    l4.place(x=110+400,y=280+100)
    Insulin=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 12),textvar=Insulin)
    Insulin.place(x=300+380,y=280+100)



    l5=tk.Label(root,text="PedigreeFunction",background="#eff0f8",font=('times', 12, ' bold '),width=14)
    l5.place(x=110+400,y=320+100)
    DiabetesPedigreeFunction=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 12),textvar=DiabetesPedigreeFunction)
    DiabetesPedigreeFunction.place(x=300+380,y=320+100)
    
    lbl = tk.Label(root, text="0 to 1"  , font=('times', 9), width=12,height=2,bg="#eff0f8",fg="grey")
    lbl.place(x=350+400, y=320+100)



    l6=tk.Label(root,text="Age",background="#eff0f8",font=('times', 12, ' bold '),width=14)
    l6.place(x=110+400,y=360+100)
    Age=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 12),textvar=Age)
    Age.place(x=300+380,y=360+100)

    

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 15, ' bold '),width=10)
    button1.place(x=230+400,y=450+100)
    
    button1 = tk.Button(root,text="<< Back",command=window,bd=0, background="#131e3a", foreground="white",font=('times', 16, ' bold '),width=10)
    button1.place(x=1270,y=10)


    root.mainloop()

Train()