def Home():
    from subprocess import call
    import tkinter as tk  
    import pandas as pd
    from PIL import Image,ImageTk
    from tkinter import ttk
    from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

    data = pd.read_csv("diabetes.csv")
    #data.head()

    data = data.dropna()


    """Feature Selection => Manual"""
    
#drop unnecessary data
    x = data.drop(['SkinThickness', 'BMI','Outcome','Pregnancies'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Outcome']
    print(type(y))
    #x.shape


#data splitting
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

   #root 
    root = tk.Tk()
    root.title("Diabetes Disease")

    w,h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry("%dx%d+0+0"%(w,h))
    #++++++++++++++++++++++++++++++++++++++++++++
    #####For background Image
    image2 =Image.open('m1.jpg')


    image2 =image2.resize((w,h), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    #background_label.image=background_image
    background_label = tk.Label(root, image=background_image)
    background_label.image=background_image

    head = tk.Label(root,text="DIABETES PREDICTION SYSTEM",width=100,height=1,font=("Tempus Sans ITC",20,"bold"),foreground="white",background="black")
    head.place(x=0,y=0)



    background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

    #_+++++++++++++++++++++++++++++++++++++++++++++++++++++++
    

    """Feature Selection => Manual"""
    


    def Data_Preprocessing():
        data = pd.read_csv("diabetes.csv")
        data.head()
        """Nukk VAlue Removal"""
        data = data.dropna()




        """Feature Selection => Manual"""
        x = data.drop(['SkinThickness', 'BMI','Outcome','Pregnancies'], axis=1)


        print(type(x))
        y = data['Outcome']
        print(type(y))
        x.shape

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)



        load = tk.Label(root,font=("Tempus Sans ITC",15,"bold"),width=50,height=2,background="green",foreground="white",text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
        load.place(x=200,y=40)


    def RF():
        
#train a Random Forest classifier, make predictions, and display the 
#classification report and accuracy

        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)
         
    #random forest
        from sklearn.ensemble import RandomForestClassifier as RF
        classifier = RF(n_estimators=14, criterion='entropy', random_state=1)
        classifier.fit(x_train,y_train)
        y_pred = classifier.predict(x_test)
        #accuracy = accuracy_score(y_test,yPred)
        

        print("=" * 40)
        print("==========")
        print("Classification Report : ",(classification_report(y_test, y_pred)))
        print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy: %.2f%%" % (accuracy * 100.0))
        ACC = (accuracy_score(y_test, y_pred) * 100)
        repo = (classification_report(y_test, y_pred))
        
        label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
        label4.place(x=205,y=100)
        
        label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as RF_MODEL.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
        label5.place(x=205,y=320)
        from joblib import dump
        dump (classifier,"RF_MODEL.joblib")
        print("Model saved as DIABETES_RF_MODEL.joblib")
        
        
        
        
    def ada():
            #start = time.time()
            dataset = pd.read_csv('diabetes.csv')
            X = dataset.iloc[:,:-1].values
            y = dataset.iloc[:,-1].values
            
            
            from sklearn.preprocessing import OneHotEncoder
            #cp
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            #restecg
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            #slope
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            #ca
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            #thal
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            
            #thal
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            
            #thal
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            
            #thal
            oneHotEncoder = OneHotEncoder()
            oneHotEncoder.fit(X)
            X = oneHotEncoder.transform(X).toarray()
            X = X[:, 0:]
            
            
    #apply standard scaling to all features (ie bring val in 0 and 1)
            from sklearn.preprocessing import StandardScaler
            scalerX = StandardScaler()
            X = scalerX.fit_transform(X)
    
    #split dataset
            from sklearn.model_selection import train_test_split
            
            XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=123)
            
            #from xgboost import XGBClassifier
            from sklearn.svm import SVC
            classifier = SVC(kernel='linear')
            classifier.fit(XTrain,yTrain)
            
    #predict data using svm
            yPred = classifier.predict(XTest)
            accuracy = accuracy_score(yTest,yPred)
            
            print("Classification Report :\n")
            repo = (classification_report(yTest, yPred))
            print(repo)
            print("Confusion Matrix :")
            cm = confusion_matrix(yTest,yPred)
            print(cm)
            print("\n")
            
            print("=" * 40)
            print("==========")
            print("Classification Report : ",(classification_report(yTest,yPred)))
            print("Accuracy : ",accuracy_score(yTest,yPred)*100)
            accuracy = accuracy_score(yTest,yPred)
            print("Accuracy: %.2f%%" % (accuracy * 100.0))
            ACC = (accuracy_score(yTest,yPred) * 100)
            repo = (classification_report(yTest,yPred))
            
            label4 = tk.Label(root,text =str(repo),width=35,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
            label4.place(x=205,y=100)
            
            label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as XGBOOST_MODEL.joblib",width=35,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
            label5.place(x=205,y=320)
            
            
    #save trained model
            from joblib import dump
            dump (classifier,"XGBOOST_MODEL.joblib")
            print("Model saved as XGBOOST_MODEL.joblib")
        
            


    def Data_Display():
       # columns = ['Age', 'Sex', 'Chest Pain', 'Rest BP', 'Chol', 'Fbs', 'Rest ECG', 'Max HR','ExAngn','OldPeak','Slope','Ca']

        data1 = pd.read_csv('diabetes.csv')
        data1['Pregnancies'] = data1['Pregnancies'][:]
        data1['Glucose'] = data1['Glucose'][:]
        data1['BloodPressure'] = data1['BloodPressure'][:]
        data1['SkinThickness'] = data1['SkinThickness'][:]
        data1['Insulin'] = data1['Insulin'][:]
        data1['BMI'] = data1['BMI'][:]
        data1['DiabetesPedigreeFunction'] = data1['DiabetesPedigreeFunction'][:]
        data1['Age'] = data1['Age'][:]
        data1['Outcome'] = data1['Outcome'][:]

        display = tk.LabelFrame(root, width=100, height=400, )
        display.place(x=200, y=400)

        tree = ttk.Treeview(display, columns=('Age', 'Sex', 'Chest Pain', 'Rest BP', 'Chol', 'Fbs', 'Rest ECG', 'Max HR','ExAng','OldPeak','Slope','Ca'))

        style = ttk.Style()
        style.configure('Treeview', rowheight=50)
        style.configure("Treeview.Heading", font=("Tempus Sans ITC", 15, "bold italic"))
        style.configure(".", font=('Helvetica', 15), background="blue")
        style.configure("Treeview", foreground='white',background="black")

        tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
        tree.column("1", width=20)
        tree.column("2", width=100)
        tree.column("3", width=100)
        tree.column("4", width=100)
        tree.column("5", width=100)
        tree.column("6", width=100)
        tree.column("7", width=100)
        tree.column("8", width=100)
        tree.column("9", width=100)

        tree.heading("1", text="Pregnancies")
        tree.heading("2", text="Glucose")
        tree.heading("3", text="BloodPressure")
        tree.heading("4", text="SkinThickness")
        tree.heading("5", text="Insulin")
        tree.heading("6", text="BMI")
        tree.heading("7", text="DiabetesPedigreeFunction")
        tree.heading("8", text="Age")
        tree.heading("9", text="Outcome")

        treeview = tree

        tree.grid(row=0, column=0, sticky=tk.NSEW)

        print("Data Displayed")
        for i in range(len(data)):
            tree.insert("", i, text=i + 1, values=(data['Pregnancies'].iloc[i],
                                                   data['Glucose'].iloc[i],
                                                   data['BloodPressure'].iloc[i],
                                                   data['SkinThickness'].iloc[i],
                                                   data['Insulin'].iloc[i],
                                                   data['BMI'].iloc[i],
                                                   data['DiabetesPedigreeFunction'].iloc[i],
                                                   data['Age'].iloc[i],
                                                   data['Outcome'].iloc[i]))



    def exit():
        root.destroy()


    def SVM_LOAD():
        call(["python","Check_Diabetes.py"])
#        import Check_Disease
#        Check_Disease.Train()
        


    button1=tk.Button(root,foreground="white",background="black",font=("Tempus Sans ITC",14,"bold"),text="Data Display",command=Data_Display,width=15,height=2)
    button1.place(x=5,y=40)

    button2=tk.Button(root,foreground="white",background="black",font=("Tempus Sans ITC",14,"bold"),text="Data_Preprocessing",command=Data_Preprocessing,width=15,height=2)
    button2.place(x=5,y=120)


    button3=tk.Button(root,foreground="white",background="black",font=("Tempus Sans ITC",14,"bold"),text="Model Training",command=ada,width=15,height=2)
    button3.place(x=5,y=200)
    

    
    button5=tk.Button(root,foreground="white",background="red",font=("Tempus Sans ITC",14,"bold"),text="Exit",command=exit,width=15,height=2)
    button5.place(x=5,y=400)
    
    button6=tk.Button(root,foreground="white",background="black",font=("Tempus Sans ITC",14,"bold"),text="Check Disease",command=SVM_LOAD,width=15,height=2)
    button6.place(x=5,y=290)
    
    

    
    root.mainloop()


    '''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''

Home()