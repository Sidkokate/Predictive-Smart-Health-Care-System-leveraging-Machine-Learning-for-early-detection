from tkinter import *
def Train():
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

    image2 = Image.open('heartbg.jpg')
    image2 = image2.resize((w,h), Image.ANTIALIAS)

    background_image = ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image

    background_label.place(x=-10, y=0)  # , relwidth=1, relheight=1)



    label_l1 = tk.Label(root, text="Check Heart Disease",font=("Times New Roman", 30, 'bold'),
                        background="#131e3a", fg="white", width=67, height=1)
    label_l1.place(x=-40, y=0)
    
    age = tk.IntVar()
    sex = tk.IntVar()
    chest_pain = tk.IntVar()
    restbp = tk.IntVar()
    chol = tk.IntVar()
    fbs = tk.IntVar()
    restecg = tk.IntVar()
    maxhr = tk.IntVar()
    exang = tk.IntVar()
    oldpeak = tk.DoubleVar()
    slope = tk.IntVar()
    ca = tk.IntVar()
    thal = tk.IntVar()
    
    
    #===================================================================================================================
    def window():
      root.destroy()
      from subprocess import call
      call(["python","main.py"])

    def Detect():
        
        
   
        e1=age.get()
        print(e1)
        e2=sex.get()
        print(e2)  
        e3=chest_pain.get()
        print(e3)
        e4=restbp.get()
        print(e4)
        e5=chol.get()
        print(e5)
        e6=fbs.get()
        print(e6)
        e7=restecg.get()
        print(e7)
        e8=maxhr.get()
        print(e8)
        e9=exang.get()
        print(e9)
        e10=oldpeak.get()
        print(e10)
        e11=slope.get()
        print(e11)
        e12=ca.get()
        print(e12)
        e13=thal.get()
        print(e13)
        #########################################################################################
        
        #pretrained model heart_disease_model.joblib(a1) is used for prediction
        from joblib import dump , load
        a1=load(r'HEART_DISEASE_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11, e12, e13]])
        print(v)    #1 is have disease, 0 means not
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Disease \nDetected!\nReport is Generated",background="red",foreground="white",font=('times', 20, ' bold '),width=15)
            yes.place(x=900,y=200)
            
            label_l1 = tk.Label(root, text="LIST OF RECOMMENDED DOCTORS\n\n  1.Dr. Khurana (9090909090) (Akurdi) \n\n  2.Dr. Jadhav (7070707070) (katraj) \n\n 3.Dr. Pawar (7878787878) (Camp) \n\n 4.Dr. Tikone (9191919191) (swargate)",font=("Times New Roman", 22, 'bold'),
                                background="#152238", fg="white", width=30, height=10)
            label_l1.place(x=900, y=310)
            
            
            file = open(r"Report.txt", 'w')
            file.write("-----Patient Report-----\n As per input data and system model Heart Disease Detected for Respective Paptient."
                       "\n***Kindly Follow Medicatins***"
                       
                    
                    )
            file.close()
            
        else:
            print("No")
            no = tk.Label(root, text="No Disease \nDetected", background="green", foreground="white",font=('times', 20, ' bold '),width=15)
            no.place(x=900, y=200)
            file = open(r"Report.txt", 'w')
            file.write("-----Patient Report-----\n As per input data and system model No Heart Disease Detected for Respective Paptient."
                       "\n\n***Relax and Follow below mentioned Life Style to be Healthy as You Are!!!***"
                        
                    
                    )
            file.close()
      



    l1 = tk.Label(root, text="Age", bd=0, background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l1.place(x=110+300, y=180-10)
    age = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=age)
    age.place(x=330-30+300, y=180-10)

    l2 = tk.Label(root, text="Gender", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l2.place(x=110+300, y=210-10)
    R1 = tk.Radiobutton(root, text="Male", background="#eff0f8", variable=sex, value=0)
    R1.place(x=330-30+300, y=210-10)
    R2 = tk.Radiobutton(root, text="Female", background="#eff0f8", variable=sex, value=1)
    R2.place(x=400-30+300, y=210-10)

    l3 = tk.Label(root, text="Chest Pain", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l3.place(x=110+300, y=240-10)
    R1 = tk.Radiobutton(root, text="Typical", background="#eff0f8", variable=chest_pain, value=1)
    R1.place(x=330-30+300, y=240-10)
    R2 = tk.Radiobutton(root, text="Asymptomatic", background="#eff0f8", variable=chest_pain, value=2)
    R2.place(x=400-30+300, y=240-10)
    R3 = tk.Radiobutton(root, text="Non-typical", background="#eff0f8", variable=chest_pain, value=3)
    R3.place(x=470-30+300, y=240-10)
    
    lbl = tk.Label(root, text="1.Typical: Pain while active   2.Atypical: Pain even when not active  3.Cannot express exactly", font=('times', 9), width=65, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=100+300, y=270-5)
    
    l4 = tk.Label(root, text="RestBP", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l4.place(x=110+300, y=300-5)
    restbp = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=restbp)
    restbp.place(x=300+300, y=300-5)
    
    lbl = tk.Label(root, text="Average value 80 - 120", font=('times', 9), width=20, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=300-5)
    
    l5 = tk.Label(root, text="Cholesterol", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l5.place(x=110+300, y=330-5)
    chol = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=chol)
    chol.place(x=300+300, y=330-5)
    
    lbl = tk.Label(root, text="Average value 200 - 240", font=('times', 9), width=20, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=330-5)
    
    l6 = tk.Label(root, text="Fasting Blood Sugar", background="#eff0f8", font=('times', 10, 'bold'), width=15)
    l6.place(x=110+300, y=360-5)
    fbs = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10))
    fbs.place(x=300+300, y=360-5)
    
    lbl = tk.Label(root, text="Average value 70 - 99", font=('times', 9), width=20, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=360-5)
    
    l7 = tk.Label(root, text="RestECG", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l7.place(x=110+300, y=390-5)
    restecg = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=restecg)
    restecg.place(x=300+300, y=390-5)
    
    lbl = tk.Label(root, text="0 to 3", font=('times', 9), width=10, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=390-5)
    
    l8 = tk.Label(root, text="Maximum Heart-rate", background="#eff0f8", font=('times', 10, 'bold'), width=15)
    l8.place(x=110+300, y=450-30)
    maxhr = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=maxhr)
    maxhr.place(x=300+300, y=450-30)
    
    lbl = tk.Label(root, text="Average = 220 - Your Age", font=('times', 9), width=20, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=450-30)
    
    l9 = tk.Label(root, text="ExANG", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l9.place(x=110+300, y=490-30)
    exang = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=exang)
    exang.place(x=300+300, y=490-30)
    
    lbl = tk.Label(root, text="0 for No Pain, 1 for Pain", font=('times', 9), width=20, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=490-30)
    
    l10 = tk.Label(root, text="Old Peak", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l10.place(x=110+300, y=520-30)
    oldpeak = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=oldpeak)
    oldpeak.place(x=300+300, y=520-30)
    
    lbl = tk.Label(root, text="Depression in range of 0.0 to 3.0", font=('times', 9), width=25, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=520-30)
    
    l11 = tk.Label(root, text="Slope in ECG", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l11.place(x=110+300, y=550-30)
    slope = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=slope)
    slope.place(x=300+300, y=550-30)
    
    lbl = tk.Label(root, text="Slope in ECG in the range of 0 to 3", font=('times', 9), width=25, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=550-30)
    
    l12 = tk.Label(root, text="Calcium", background="#eff0f8", font=('times', 10, 'bold'), width=10)
    l12.place(x=110+300, y=580-30)
    ca = tk.Entry(root, bd=2, width=5, font=("TkDefaultFont", 10), textvar=ca)
    ca.place(x=300+300, y=580-30)
    
    lbl = tk.Label(root, text="Calcium in range of 0 to 3", font=('times', 9), width=20, height=1, bg="#eff0f8", fg="grey")
    lbl.place(x=350+300, y=580-30)
    
    l13 = tk.Label(root, text="Thallium", background="white", font=('times', 10, 'bold'), width=10)
    l13.place(x=110+300, y=610-30)
    R4 = tk.Radiobutton(root, text="Fixed", variable=thal, background="#eff0f8", value=1)
    R4.place(x=300+300, y=610-30)
    R5 = tk.Radiobutton(root, text="Normal", variable=thal, background="#eff0f8", value=2)
    R5.place(x=370+300, y=610-30)
    R6 = tk.Radiobutton(root, text="Reversible", variable=thal, background="#eff0f8", value=3)
    R6.place(x=440+300, y=610-30)
    
    #lbl = tk.Label(root, text="Normal, Fixed: Blood flow less always, Reversible: Irregular blood flow", font=('times', 9), width=65, height=1, bg="#eff0f8", fg="grey")
    #lbl.place(x=100+400, y=640-30)
    
    button1 = tk.Button(root, text="Submit", command=Detect, font=('times', 15, 'bold'), width=10)
    button1.place(x=700+150, y=350)

    button1 = tk.Button(root, text="<<  Back", command=window, bd=0, background="#131e3a", foreground="white", font=('times', 16, 'bold'), width=10)
    button1.place(x=1220, y=10)

    


    root.mainloop()

Train()