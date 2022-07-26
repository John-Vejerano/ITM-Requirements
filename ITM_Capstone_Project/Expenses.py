from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql
import os

#main loop

class ConnectorDB:
    def __init__(self, root):
        self.root = root
        titlespace = " "
        self.root.title(0 * titlespace + "Sample Business GUI")
        self.root.geometry("1350x675+100+0")
        self.root.resizable(width=False, height=False)

    
#Window Design

        MainFrame = Frame(self.root, bd =10, width = 2000, height = 700, relief = RIDGE, bg = '#ECB390')
        MainFrame.grid()

        titlespace = Frame(MainFrame, bd = 7, width = 1900, height = 200,padx = 2, relief = RIDGE,bg = '#FCF8E8')
        titlespace.grid(row = 0, column = 0)

        
        TopFrame = Frame(MainFrame, bd = 5, width = 2000, height = 700, bg = '#94B49F', relief = RIDGE)
        TopFrame.grid(row = 1, column = 0)
        TopFrame2 = Frame(MainFrame, bd = 5, width = 2000, height = 700, bg = '#94B49F', relief = RIDGE)
        TopFrame2.grid(row = 1, column = 1)


        RightFrame = Frame(TopFrame, bd =5, width = 900, height = 100, padx = 2, bg = '#ECB390', relief = RIDGE)
        RightFrame.pack(side = RIGHT)
        
        RightFrame1 = Frame(RightFrame, bd = 5, width = 1000, height = 100, padx = 12, pady = 24, relief = RIDGE,bg = '#FCF8E8')
        RightFrame1.pack(side = TOP)

        RightFrame2 = Frame(TopFrame2, bd = 5, width = 200, height = 700, padx = 0, pady = 24, relief = RIDGE,bg = '#94B49F')
        RightFrame2.pack(side = RIGHT)

        RightFrame3 = Frame(RightFrame2, bd = 5, width = 200, height = 500, padx = 2, pady = 2, relief = RIDGE,bg = '#94B49F')
        RightFrame3.pack(side = RIGHT)


        LeftFrame1 = Frame(TopFrame, bd = 5, width = 800, height = 100, padx = 2, bg = '#94B49F', relief = RIDGE)
        LeftFrame1.pack(side = LEFT)
        
        LeftFrame2 = Frame(LeftFrame1, bd = 5, width = 200, height = 500, padx = 2, pady = 2, bg = '#94B49F', relief = RIDGE)
        LeftFrame2.pack(side = TOP)

        self.maintitle = Label(titlespace, font = ('Times New Roman',40,'bold'),text = 'Expenses Database', bd=10, bg = "#FCF8E8")
        self.maintitle.grid(row = 0,column = 0, padx = 200)

#Textbox string variables
        Expense_ID = StringVar()
        Expense_Type = StringVar()
        Expense_Price = StringVar()
        Expense_Quantity = StringVar()
        Month = StringVar()
        Year = StringVar()
        Day = StringVar()

#labels and entry widgets
        self.lblExpense_ID = Label(RightFrame1,font=('Times New Roman', 12, 'bold'),text="Expense ID",bd=7,bg="#FCF8E8")
        self.lblExpense_ID.grid(row=0, column=0, sticky=W, padx=100)
        self.entExpense_ID = Entry(RightFrame1,font=('Times New Roman', 12, 'bold'),bd=5,width=44,justify='left',textvariable=Expense_ID)
        self.entExpense_ID.grid(row=0, column=1, sticky=W, padx=100)

        self.lblExpense_Type = Label(RightFrame1,font=('Times New Roman', 12, 'bold'),text="Expense Type",bd=7,bg="#FCF8E8")
        self.lblExpense_Type.grid(row=1, column=0, sticky=W, padx=100)
        self.entExpense_Type = Entry(RightFrame1,font=('Times New Roman', 12, 'bold'),bd=5,width=44,justify='left',textvariable=Expense_Type)
        self.entExpense_Type.grid(row=1, column=1, sticky=W, padx=100)

        self.lblExpense_Price = Label(RightFrame1,font=('Times New Roman', 12, 'bold'),text="Expense Price",bd=7,bg="#FCF8E8")
        self.lblExpense_Price.grid(row=2, column=0, sticky=W, padx=100)
        self.entExpense_Price = Entry(RightFrame1,font=('Times New Roman', 12, 'bold'),bd=5,width=44,justify='left',textvariable=Expense_Price)
        self.entExpense_Price.grid(row=2, column=1, sticky=W, padx=100)

        self.lblExpense_Quantity = Label(RightFrame1,font=('Times New Roman', 12, 'bold'),text="Expense Quantity",bd=7,bg="#FCF8E8")
        self.lblExpense_Quantity.grid(row=3, column=0, sticky=W, padx=100)
        self.entExpense_Quantity = Entry(RightFrame1,font=('Times New Roman', 12, 'bold'),bd=5,width=3,justify='left',textvariable=Expense_Quantity)
        self.entExpense_Quantity.grid(row=3, column=1, sticky=W, padx=100)

        self.Date = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Day/Month/Year", bd = 7, bg = "#FCF8E8")
        self.Date.grid(row = 4, column = 0, sticky = W, padx = 100)
        self.entDay = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Day)
        self.entDay.grid(row = 4, column = 1, sticky = W, padx = 100)
        self.entMonth = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Month)
        self.entMonth.grid(row = 4, column = 1, sticky = W, padx = 150)
        self.entYear = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Year)
        self.entYear.grid(row = 4, column = 1, sticky = W, padx = 200)

#Treeview table
        scroll_y = Scrollbar(RightFrame, orient=VERTICAL)

        self.expenses_records = ttk.Treeview(RightFrame,height=14,columns=("Expense_ID", "Expense_Type","Expense_Price", "Expense_Quantity", "Day", "Month","Year"),yscrollcommand=scroll_y.set) 
        scroll_y.pack(side=RIGHT, fill=Y)

        self.expenses_records.heading("Expense_ID",text="Expense ID")

        self.expenses_records.heading("Expense_Type", text="Expense Type")
        self.expenses_records.heading("Expense_Price", text="Expense Price")
        self.expenses_records.heading("Expense_Quantity",
                                         text="Expense Quantity")
        self.expenses_records.heading("Day", text="Day")
        self.expenses_records.heading("Month", text="Month")
        self.expenses_records.heading("Year", text="Year")

        self.expenses_records['show'] = 'headings'
        self.expenses_records.column("Expense_ID", width=120)
        self.expenses_records.column("Expense_Type", width=120)
        self.expenses_records.column("Expense_Price", width=120)
        self.expenses_records.column("Expense_Quantity", width=120)
        self.expenses_records.column("Day", width=50)
        self.expenses_records.column("Month", width=50)
        self.expenses_records.column("Year", width=50)

        self.expenses_records.pack(fill=BOTH, expand=1)

#Button Commands

        def Reset():
            self.entExpense_ID.delete(0, END)
            self.entExpense_Type.delete(0, END)
            self.entExpense_Price.delete(0, END)
            self.entExpense_Quantity.delete(0, END)
            self.entMonth.delete(0, END)
            self.entDay.delete(0, END)
            self.entYear.delete(0, END)
        def Exit():
            Exit = tkinter.messagebox.askyesno("Sample Business GUI","Confirm Exit")
            if Exit > 0:
                root.destroy()
                return
        def addData():
            if Expense_ID.get() =="" or Expense_Type.get() =="" or Expense_Quantity.get() =="" or Expense_Price.get() =="" or Day.get() == ""or Month.get() == ""or Year.get() == "":
                tkinter.messagebox.askyesno("Sample Business GUI", "Enter Correct Details")
                Reset()
            else:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("insert into expenses values(%s,%s,%s,%s,%s,%s,%s)", (

                Expense_ID.get(),
                Expense_Type.get(),
                Expense_Price.get(),
                Expense_Quantity.get(),
                Day.get(),
                Month.get(),
                Year.get()
                
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Sample Business GUI", "Record Entered Successfully")
                Reset()
        def clear_all():
            for item in self.expenses_records.get_children():
                self.expenses_records.delete(item)
        def DisplayData():
                clear_all()
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("select * from expenses")
                result = cur.fetchall()
                if len(result) != 0:
                    self.expenses_records.delete(*self.expenses_records.get_children())
                    for row in result:
                        self.expenses_records.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()

        def ExpenseInfo(ev):
            viewInfo = self.expenses_records.focus()
            learnerData = self.expenses_records.item(viewInfo)
            row = learnerData['values']
            Expense_ID.set(row[0]),
            Expense_Type.set(row[1]),
            Expense_Price.set(row[2])
            Expense_Quantity.set(row[3])

        


        def Update():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("update expenses set expense_type = %s, expense_price = %s, expense_quantity = %s,month = %s, year = %s, day = %s where expense_id = %s", (Expense_Type.get(),Expense_Price.get(),Expense_Quantity.get(),Month.get(),Year.get(),Day.get(),Expense_ID.get()))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Sample Business GUI", "Record Updated Successfully")
                Reset()
            except:
                tkinter.messagebox.askyesno("Sample Business GUI", "Enter Correct Details")
                Reset()
            
               
        def DeleteDB():
            try:
                if Expense_ID.get() =="":
                    tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                    Reset()
                else:
                    sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                    cur = sqlCon.cursor()
                    cur.execute("delete from expenses where expense_id = %s", Expense_ID.get())

                    sqlCon.commit()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Sample Business GUI", "Record Deleted Successfully")
                    Reset()
            except:
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()

        
        
        def SearchDB():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("select * from expenses where expense_id =%s"%Expense_ID.get())

                row = cur.fetchone()
                
                Expense_ID.set(row[0]),
                Expense_Type.set(row[1]),
                Expense_Price.set(row[2])
                Expense_Quantity.set(row[3])
                self.entMonth.delete(0, END)
                self.entDay.delete(0, END)
                self.entYear.delete(0, END)
                sqlCon.commit() 
                sqlCon.close()

            except:   
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()

        def Products():
            os.startfile("Products.exe")
            root.destroy()
        
        def Customers():
            os.startfile("Customers.exe")
            root.destroy()
        
        self.expenses_records.bind("<ButtonRelease-1>", ExpenseInfo)
            

#Buttons

        self.btnAdd = Button(LeftFrame2,font=('times new roman', 16, 'bold'),text="Add",bd=1,pady=1,padx=10,width=8,height=2,bg="#CEE5D0",command = addData).grid(row=1, column=0, padx=1)
        self.btnDelete = Button(LeftFrame2,font=('times new roman', 16, 'bold'),text="Delete",bd=1,pady=1,padx=10,width=8,height=2,bg="#CEE5D0",command = DeleteDB).grid(row=2, column=0, padx=1)
        self.btnReset = Button(LeftFrame2,font=('times new roman', 16, 'bold'),text="Reset",bd=1,pady=1,padx=10,width=8,height=2,bg="#CEE5D0",command=Reset).grid(row=3, column=0, padx=1)
        self.btnSearch = Button(LeftFrame2,font=('times new roman', 16, 'bold'),text="Search",bd=1,pady=1,padx=10,width=8,height=2,bg="#CEE5D0",command = SearchDB).grid(row=4, column=0, padx=1)
        self.btnDisplay = Button(LeftFrame2,font=('times new roman', 16, 'bold'),text="Display",bd=1,pady=1,padx=10,width=8,height=2,bg="#CEE5D0",command=DisplayData).grid(row=5, column=0, padx=1)
        self.btnUpdate = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Update", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Update).grid(row = 6, column = 0, padx = 1)
        self.btnExit = Button(LeftFrame2,font=('times new roman', 16, 'bold'),text="Exit",bd=1,pady=1,padx=10,width=8,height=2,bg="#CEE5D0", command = Exit).grid(row=7, column=0, padx=1)
        self.btnExpenses = Button(RightFrame3,font=('times new roman', 20, 'bold'),text="Expenses",bd=1,pady=1,padx=10,width=10,height=3,bg="#CEE5D0").grid(row=0, column=0)
        self.btnProducts = Button(RightFrame3,font=('times new roman', 20, 'bold'),text="Products",bd=1,pady=1,padx=10,width=10,height=3,bg="#CEE5D0", command = Products).grid(row=2, column=0)
        self.btnCustomers = Button(RightFrame3,font=('times new roman', 20, 'bold'),text="Customers",bd=1,pady=1,padx=10,width=10,height=3,bg="#CEE5D0",command = Customers).grid(row=3, column=0)



if __name__ == '__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
