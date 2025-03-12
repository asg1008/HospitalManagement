from tkinter import*
from tkinter import ttk, Label
from tkinter import messagebox
import time
import datetime
import random
import math
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x750+0+0")


        self.nameoftab=StringVar()
        self.refer=StringVar()
        self.dose=StringVar()
        self.nooftab=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect=StringVar()
        self.driving=StringVar()
        self.storageadv=StringVar()
        self.medication=StringVar()
        self.patientID=StringVar()
        self.nhs=StringVar()
        self.patientname=StringVar()
        self.dob=StringVar()
        self.patientadd=StringVar()



        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)


       # ================Data Frame==================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1540,height=400)

        dataframeleft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",22,"bold"),bg="white",text="Patient Information")
        dataframeleft.place(x=0,y=5,width=900,height=350)
        

        dataframert=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,
                                 font=("times new roman",22,"bold"),bg="white",text="Prescription")
        dataframert.place(x=980,y=5,width=420,height=350)


        #=================Button frame================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1540,height=75)


        #=================Details frame================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1540,height=160)

        #==========DataFrameLeft===========================
        lblNAme=Label(dataframeleft,text="Names of tablet",font=("times new roman",12,"bold"),padx=2,pady=5)
        lblNAme.grid(row=0,column=0,sticky=W)

        comName=ttk.Combobox(dataframeleft,textvariable=self.nameoftab,font=("times new roman",12,"bold"),width=33)
        comName['values']=('Vaccine','Paracetamol','Ibuprofen','Aspir')
        comName.grid(row=0,column=1)

        lblref=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Reference Number:",padx=2,pady=5)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(dataframeleft,textvariable=self.refer,font=("times new roman",12,"bold"),width=35)
        txtref.grid(row=1,column=1)

        lbldose=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Dose:",padx=2,pady=5)
        lbldose.grid(row=2,column=0,sticky=W)
        txtd=Entry(dataframeleft,textvariable=self.dose,font=("times new roman",12,"bold"),width=35)
        txtd.grid(row=2,column=1)

        lblnt=Label(dataframeleft,font=("times new roman", 12, "bold"),text="No of tablets:",padx=2,pady=5)
        lblnt.grid(row=3,column=0,sticky=W)
        txtnt=Entry(dataframeleft, textvariable=self.nooftab,font=("times new roman",12,"bold"),width=35)
        txtnt.grid(row=3,column=1)

        lblissue=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Issue Date:",padx=2,pady=5)
        lblissue.grid(row=4,column=0,sticky=W)
        txti=Entry(dataframeleft,textvariable=self.issuedate,font=("times new roman",12,"bold"),width=35)
        txti.grid(row=4,column=1)

        lblexp=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Expiry Date:",padx=2,pady=5)
        lblexp.grid(row=5,column=0,sticky=W)
        txtex=Entry(dataframeleft,textvariable=self.expdate,font=("times new roman",12,"bold"),width=35)
        txtex.grid(row=5,column=1)

        lbldosed=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Daily Dose:",padx=2,pady=5)
        lbldosed.grid(row=6,column=0,sticky=W)
        txtdd=Entry(dataframeleft,textvariable=self.dailydose,font=("times new roman",12,"bold"),width=35)
        txtdd.grid(row=6,column=1)

        lbleff=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Side Effect:",padx=2,pady=5)
        lbleff.grid(row=7,column=0,sticky=W)
        txteff=Entry(dataframeleft,textvariable=self.sideeffect,font=("times new roman",12,"bold"),width=35)
        txteff.grid(row=7,column=1)

        lblbp=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Blood Pressure:",padx=2)
        lblbp.grid(row=0,column=2,sticky=W)
        txtbp=Entry(dataframeleft,textvariable=self.driving,font=("times new roman",12,"bold"),width=35)
        txtbp.grid(row=0,column=3)

        lbladvice=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Storage Advice:",padx=2)
        lbladvice.grid(row=1,column=2,sticky=W)
        txtadvvice=Entry(dataframeleft,textvariable=self.storageadv,font=("times new roman",12,"bold"),width=35)
        txtadvvice.grid(row=1,column=3)

        lblmed=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Medication:",padx=2)
        lblmed.grid(row=2,column=2,sticky=W)
        txtmed=Entry(dataframeleft,textvariable=self.medication,font=("times new roman",12,"bold"),width=35)
        txtmed.grid(row=2,column=3)

        lblpID=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Patient ID:",padx=2)
        lblpID.grid(row=3,column=2,sticky=W)
        txtpID=Entry(dataframeleft,textvariable=self.patientID,font=("times new roman",12,"bold"),width=35)
        txtpID.grid(row=3,column=3)
        
        lblnhs=Label(dataframeleft,font=("times new roman", 12, "bold"),text="NHS Number:",padx=2)
        lblnhs.grid(row=4,column=2,sticky=W)
        txtnhs=Entry(dataframeleft,textvariable=self.nhs,font=("times new roman",12,"bold"),width=35)
        txtnhs.grid(row=4,column=3)

        lblpName=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Patient Name:",padx=2)
        lblpName.grid(row=5,column=2,sticky=W)
        txtpName=Entry(dataframeleft,textvariable=self.patientname,font=("times new roman",12,"bold"),width=35)
        txtpName.grid(row=5,column=3)

        lbldob=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Date of Birth:",padx=2)
        lbldob.grid(row=6,column=2,sticky=W)
        txtdob=Entry(dataframeleft,textvariable=self.dob,font=("times new roman",12,"bold"),width=35)
        txtdob.grid(row=6,column=3)

        lblpadd=Label(dataframeleft,font=("times new roman", 12, "bold"),text="Patient Address:",padx=2)
        lblpadd.grid(row=7,column=2,sticky=W)
        txtpadd=Entry(dataframeleft,textvariable=self.patientadd,font=("times new roman",12,"bold"),width=35)
        txtpadd.grid(row=7,column=3)

        #=======================DataFrame Right====================
        self.txtPres=Text(dataframert,font=("times new roman",12,"bold"),width=43,height=14,padx=2,pady=6)
        self.txtPres.grid(row=0,column=0)

        #==========Buttons=============================
        btnPres=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("times new roman",12,"bold"),width=20,command=self.presdata)
        btnPres.grid(row=0,column=0)

        btnPresData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("times new roman",12,"bold"),width=20,command=self.iPresData)
        btnPresData.grid(row=0,column=1)

        btnupdate=Button(Buttonframe, command= self.update_data,text="Update",bg="green",fg="white",font=("times new roman",12,"bold"),width=20)
        btnupdate.grid(row=0,column=2)

        btndel=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("times new roman",12,"bold"),width=20,command=self.delete)
        btndel.grid(row=0,column=3)

        btnclear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("times new roman",12,"bold"),width=20,command=self.clear)
        btnclear.grid(row=0,column=4)

        btnexit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("times new roman",12,"bold"),width=20,command=self.exit)
        btnexit.grid(row=0,column=5)


        #========================Table==============================

        #=============================scroll bar=============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)

        self.hosp_table = ttk.Treeview(Detailsframe, column=("nameoftablet", "ref", "dose", "nooftablet", "issue", "exp", "Daily", "side", "BP", "storage", "med", "pid", "nhs", "pname", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hosp_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hosp_table.yview)

        self.hosp_table.heading("nameoftablet",text="Name of Tablets")
        self.hosp_table.heading("ref",text="Reference")
        self.hosp_table.heading("dose",text="Dose")
        self.hosp_table.heading("nooftablet",text="No of Tablets")
        self.hosp_table.heading("issue",text="Issue Date")
        self.hosp_table.heading("exp",text="Expiry Date")
        self.hosp_table.heading("Daily",text="Daily Dosage")
        self.hosp_table.heading("side",text="Side Effect")
        self.hosp_table.heading("BP",text="Blood Pressure")
        self.hosp_table.heading("storage",text="Storage")
        self.hosp_table.heading("med",text="Medication")
        self.hosp_table.heading("pid",text="Patient ID")
        self.hosp_table.heading("nhs",text="NHS Number")
        self.hosp_table.heading("pname",text="Patient Name")
        self.hosp_table.heading("dob",text=" Date of Birth")
        self.hosp_table.heading("address",text=" Address")


        self.hosp_table['show']='headings'
        

        self.hosp_table.column("nameoftablet",width=100)
        self.hosp_table.column("ref",width=100)
        self.hosp_table.column("dose",width=100)
        self.hosp_table.column("nooftablet",width=100)
        self.hosp_table.column("issue",width=100)
        self.hosp_table.column("exp",width=100)
        self.hosp_table.column("Daily",width=100)
        self.hosp_table.column("side",width=100)
        self.hosp_table.column("BP",width=100)
        self.hosp_table.column("storage",width=100)
        self.hosp_table.column("med",width=100)
        self.hosp_table.column("pid",width=100)
        self.hosp_table.column("nhs",width=100)
        self.hosp_table.column("pname",width=100)
        self.hosp_table.column("dob",width=100)
        self.hosp_table.column("address",width=100)


        self.hosp_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.hosp_table.bind("<ButtonRelease-1>",self.get_cursor)


        #=====================Funtionality=========================
    def iPresData(self):
        if self.nameoftab.get()=="" or self.refer.get()==" ":
                messagebox.showerror("Error","Please fill all fields")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", port=3306, password="admin", database="mydb")
                cur = conn.cursor()
                cur.execute("INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
                    (self.nameoftab.get(), self.refer.get(), self.dose.get(), self.nooftab.get(), self.issuedate.get(),
                         self.expdate.get(), self.dailydose.get(), self.sideeffect.get(), self.driving.get(), self.storageadv.get(),
                         self.medication.get(), self.patientID.get(), self.nhs.get(), self.patientname.get(), self.dob.get(),
                         self.patientadd.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Data inserted successfully")
            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database error: {e}")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {e}")


    def update_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", port=3306, password="admin", database="mydb")
        cur = conn.cursor()
        cur.execute("UPDATE hospital SET Name_of_Tablets=%s, Dose=%s, No_of_tablet=%s,  Issue=%s, Expiry=%s, daily=%s, Storage=%s, NHS=%s, Patient_NAme=%s, DOB=%s, Patient_Address=%s, side_effect=%s, BP=%s, Medication=%s, Pat_ID=%s WHERE Reference=%s",(
            self.nameoftab.get(), self.dose.get(), self.nooftab.get(), self.issuedate.get(), self.expdate.get(), self.dailydose.get(), self.storageadv.get(), self.nhs.get(), 
            self.patientname.get(), self.dob.get(), self.patientadd.get(), self.sideeffect.get(), self.driving.get(), self.medication.get(), self.patientID.get(), self.refer.get(),)) 
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Data updated successfully")
      

        
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", port=3306, password
                                        ="admin", database="mydb")
        cur = conn.cursor()
        cur.execute("SELECT * FROM hospital")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.hosp_table.delete(*self.hosp_table.get_children())
            for row in rows:
                self.hosp_table.insert('', 'end', values=row)
        conn.commit()
        conn.close()


    def get_cursor(self,event):
        cur_row=self.hosp_table.focus()
        contents=self.hosp_table.item(cur_row)
        row=contents['values']
        self.nameoftab.set(row[0])
        self.refer.set(row[1])
        self.dose.set(row[2])
        self.nooftab.set(row[3])
        self.issuedate.set(row[4])
        self.expdate.set(row[5])
        self.dailydose.set(row[6])
        self.sideeffect.set(row[7])
        self.driving.set(row[8])
        self.storageadv.set(row[9])
        self.medication.set(row[10])
        self.patientID.set(row[11])
        self.nhs.set(row[12])
        self.patientname.set(row[13])
        self.dob.set(row[14])
        self.patientadd.set(row[15])
        


    def presdata(self):
        self.txtPres.insert(END,"Name of Tablets: \t\t "+self.nameoftab.get()+"\n")
        self.txtPres.insert(END,"Reference Number: \t\t "+self.refer.get()+"\n")
        self.txtPres.insert(END,"Dose: \t\t "+self.dose.get()+"\n")
        self.txtPres.insert(END,"No of Tablets: \t\t "+self.nooftab .get()+"\n")
        self.txtPres.insert(END,"Issue Date: \t\t "+self.issuedate.get()+" \n")
        self.txtPres.insert(END,"Expiry Date: \t\t "+self.expdate.get()+" \n")
        self.txtPres.insert(END,"Daily Dose: \t\t "+self.dailydose.get ()+" \n")
        self.txtPres.insert(END,"Side Effects: \t\t "+self.sideeffect.get()+" \n")
        self.txtPres.insert(END,"Driving: \t\t "+self.driving.get()+" \n ")
        self.txtPres.insert(END,"Storage Advice: \t\t "+self.storageadv.get()+" \n ")
        self.txtPres.insert(END,"Medication: \t\t "+self.medication.get()+" \n ")
        self.txtPres.insert(END,"Patient ID: \t\t "+self.patientID.get()+" \n ")
        self.txtPres.insert(END,"NHS Number: \t\t "+self.nhs.get()+" \n ")
        self.txtPres.insert(END,"Patient Name: \t\t "+self.patientname.get()+" \n ")
        self.txtPres.insert(END,"Date of Birth: \t\t "+self.dob.get()+" \n ")
        self.txtPres.insert(END,"Patient Address: \t\t "+self.patientadd.get()+" \n ")


    def delete (self):
        conn = mysql.connector.connect(host="localhost", username="root", port=3306, password="admin", database="mydb")
        cur = conn.cursor()
        cur.execute("DELETE FROM hospital WHERE Reference=%s", (self.refer.get(),))
        conn.commit()
        conn.close()

        
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")


    def clear(self):
        self.nameoftab.set("")
        self.refer.set("")
        self.dose.set("")
        self.nooftab.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.sideeffect.set("")
        self.driving.set("")
        self.storageadv.set("")
        self.medication.set("")
        self.patientID.set("")
        self.nhs.set("")
        self.patientname.set("")
        self.dob.set("")
        self.patientadd.set("")
        self.txtPres.delete(1.0,END)
        

    def exit(self):
        exit=messagebox.askyesno("Ask ","Do you want to exit?")
        if exit>0:
            self.root.destroy()
            return



root=Tk()
obj=Hospital(root)
root.mainloop()