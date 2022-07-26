from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import os

class ConnectorDB:
    #mainloop
    def __init__(self,root):
        #title
        self.root = root
        titlespace = " "
        self.root.title(0 * titlespace + "Sample Business GUI")
        self.root.geometry("1355x815+100+0")
        self.root.resizable(width = False, height = False)
        
        #frames and main window design
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

        #main header

        self.maintitle = Label(titlespace, font = ('Times New Roman',40,'bold'),text = 'Customer Database', bd=10, bg = "#FCF8E8")
        self.maintitle.grid(row = 0,column = 0, padx = 200)

        

        #string values on textboxes
        Customer_FName = StringVar()
        Customer_LName = StringVar()
        Month = StringVar()
        Year = StringVar()
        Day = StringVar()
        Transaction_ID = StringVar()
        Cell_Num = StringVar()
        C_Email = StringVar()
        Order_Type = StringVar()
        Quantity = StringVar()

        #labels of textboxes and textboxes
        self.lblTransaction_ID = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Transaction ID", bd = 7, bg = "#FCF8E8")
        self.lblTransaction_ID.grid(row = 0, column = 0, sticky = W, padx = 100)
        self.entTransaction_ID = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Transaction_ID)
        self.entTransaction_ID.grid(row = 0, column = 1, sticky = W, padx = 100)

        self.lblCustomer_FName = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "First Name", bd = 7, bg = "#FCF8E8")
        self.lblCustomer_FName.grid(row = 1, column = 0, sticky = W, padx = 100)
        self.entCustomer_FName = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Customer_FName)
        self.entCustomer_FName.grid(row = 1, column = 1, sticky = W, padx = 100)

        self.lblCustomer_LName = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Last Name", bd = 7, bg = "#FCF8E8")
        self.lblCustomer_LName.grid(row = 2, column = 0, sticky = W, padx = 100)
        self.entCustomer_LName = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Customer_LName)
        self.entCustomer_LName.grid(row = 2, column = 1, sticky = W, padx = 100)

        self.lblCell_Num = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Cellphone Number", bd = 7, bg = "#FCF8E8")
        self.lblCell_Num.grid(row = 3, column = 0, sticky = W, padx = 100)
        self.entCell_Num = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Cell_Num)
        self.entCell_Num.grid(row = 3, column = 1, sticky = W, padx = 100)

        self.C_Email = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Email", bd = 7, bg = "#FCF8E8")
        self.C_Email.grid(row = 4, column = 0, sticky = W, padx = 100)
        self.entC_Email = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = C_Email)
        self.entC_Email.grid(row = 4, column = 1, sticky = W, padx = 100)

        self.Transaction = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Transaction:", bd = 7, bg = "#FCF8E8")
        self.Transaction.grid(row = 5, column = 0, sticky = W, padx = 100)

        self.Order_Type = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Order", bd = 7, bg = "#FCF8E8")
        self.Order_Type.grid(row = 6, column = 0, sticky = W, padx = 100)
        self.entOrder_Type = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Order_Type)
        self.entOrder_Type.grid(row = 6, column = 1, sticky = W, padx = 100)

        self.Quantity = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Quantity", bd = 7, bg = "#FCF8E8")
        self.Quantity.grid(row = 7, column = 0, sticky = W, padx = 100)
        self.entQuantity = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Quantity)
        self.entQuantity.grid(row = 7, column = 1, sticky = W, padx = 100)



        self.Date = Label(RightFrame1, font = ('Times New Roman', 12, 'bold'), text = "Day/Month/Year", bd = 7, bg = "#FCF8E8")
        self.Date.grid(row = 8, column = 0, sticky = W, padx = 100)
        self.entDay = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Day)
        self.entDay.grid(row = 8, column = 1, sticky = W, padx = 100)
        self.entMonth = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Month)
        self.entMonth.grid(row = 8, column = 1, sticky = W, padx = 150)
        self.entYear = Entry(RightFrame1, font = ('Times New Roman', 12, 'bold'), bd = 5, width = 2, justify = 'left', textvariable = Year)
        self.entYear.grid(row = 8, column = 1, sticky = W, padx = 200)

        

 #code for table at the bottom

        scroll_y = Scrollbar(RightFrame, orient = VERTICAL)
        
        self.transaction_records = ttk.Treeview(RightFrame, height = 14, columns = ("Customer_FName", "Customer_LName", "Transaction_ID", "C_Email","Cell_Num","Order_Type","Quantity","Day","Month","Year"), yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT, fill = Y)

        self.transaction_records.heading("Transaction_ID", text="Transaction ID")
        self.transaction_records.heading("Customer_LName", text="Customer Last Name")
        self.transaction_records.heading("Customer_FName", text="Customer First Name")
        self.transaction_records.heading("C_Email", text="Customer Email")
        self.transaction_records.heading("Cell_Num", text="Cellphone Number")
        self.transaction_records.heading("Day", text="Day")
        self.transaction_records.heading("Month", text="Month")
        self.transaction_records.heading("Year", text="Year")
        self.transaction_records.heading("Order_Type", text="Order Type")
        self.transaction_records.heading("Quantity", text="Quantity")


        self.transaction_records['show'] = 'headings'

        self.transaction_records.column("Transaction_ID", width = 120)
        self.transaction_records.column("Customer_LName", width = 120)
        self.transaction_records.column("Customer_FName", width = 120)
        self.transaction_records.column("C_Email", width = 120)
        self.transaction_records.column("Cell_Num", width = 120)  
        self.transaction_records.column("Day", width = 50)
        self.transaction_records.column("Month", width = 50)
        self.transaction_records.column("Year", width = 50)
        self.transaction_records.column("Order_Type", width = 120)
        self.transaction_records.column("Quantity", width = 50)

        self.transaction_records.pack(fill = BOTH, expand = 1)


 #button functions

        def Reset():
            self.entTransaction_ID.delete(0, END)
            self.entCustomer_FName.delete(0, END)
            self.entCustomer_LName.delete(0, END)
            self.entC_Email.delete(0, END)
            self.entCell_Num.delete(0, END)
            self.entOrder_Type.delete(0, END)
            self.entMonth.delete(0, END)
            self.entDay.delete(0, END)
            self.entYear.delete(0, END)
            self.entQuantity.delete(0, END)

        def Exit():
            Exit = tkinter.messagebox.askyesno("Sample Business GUI", "Confirm exit")
            if Exit > 0:
                root.destroy()
                return
        def clear_all():
            for item in self.transaction_records.get_children():
                self.transaction_records.delete(item)
        def addData():
            try:
        
                if Customer_FName.get() =="" or Customer_LName.get() =="" or Month.get() =="" or Year.get() =="" or Day.get() =="" or C_Email.get() ==""or Quantity.get() =="":
                    tkinter.messagebox.askyesno("Sample Business GUI", "Enter Correct Details")
                    Reset()
                else:
                    sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                    cur = sqlCon.cursor()
                    cur.execute("insert into customers values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (Customer_FName.get(),Customer_LName.get(),Transaction_ID.get(),C_Email.get(), Cell_Num.get(),Order_Type.get(),Quantity.get(),Day.get(),Month.get(),Year.get()))
                    sqlCon.commit()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Sample Business GUI", "Record Entered Successfully")
                    Reset()
            except:
                tkinter.messagebox.askyesno("Sample Business GUI", "Enter Correct Details")
                Reset()
        def DisplayData():
                clear_all()
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("select * from customers")
                result = cur.fetchall()
                if len(result) != 0:
                    self.transaction_records.delete(*self.transaction_records.get_children())
                    for row in result:
                        self.transaction_records.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()

        def Delete():
            try:
        
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("delete from customers where Transaction_ID = %s", Transaction_ID.get())
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Sample Business GUI", "Record Deleted Successfully")
                Reset()
            except:
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()

        def Update():
            try:
                if Transaction_ID.get() =="":
                    tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                    Reset()
                else:
                    sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                    cur = sqlCon.cursor()
                    cur.execute("update customers set First_Name = %s, Last_Name = %s, Email = %s, Number = %s, Order_Type=%s, Quantity = %s,Month = %s, Year = %s, Day = %s where Transaction_ID = %s", (Customer_FName.get(),Customer_LName.get(),C_Email.get(), Cell_Num.get(),Order_Type.get(),Quantity.get(),Month.get(),Year.get(),Day.get(),Transaction_ID.get()))
                    sqlCon.commit()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Sample Business GUI", "Record Updated Successfully")
            except:
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()
        def SearchDB():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("select * from customers where Transaction_ID = '%s'"%Transaction_ID.get())

                row = cur.fetchone()
                
                Transaction_ID.set(row[2]),
                Customer_FName.set(row[0]),
                Customer_LName.set(row[1]),
                C_Email.set(row[3]),
                Cell_Num.set(row[4]),
                Order_Type.set(row[5])
                Quantity.set(row[6])
                self.entMonth.delete(0, END)
                self.entDay.delete(0, END)
                self.entYear.delete(0, END)
                sqlCon.commit() 
            except:   
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()
            sqlCon.close()
        def TransactionInfo(ev):
            viewInfo = self.transaction_records.focus()
            learnerData = self.transaction_records.item(viewInfo)
            row = learnerData['values']
            Transaction_ID.set(row[2]),
            Customer_FName.set(row[0]),
            Customer_LName.set(row[1]),
            C_Email.set(row[3]),
            Cell_Num.set(row[4]),
            Order_Type.set(row[5])
            Quantity.set(row[6])

        def Cost():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("select * from products where product_id =%s"%Order_Type.get())
                price = cur.fetchone()
                tkinter.messagebox.showinfo("Sample Business GUI", price[1] + " Php" + str(price[2]))
                
            except:
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()

        def Expenses():
            os.startfile("Expenses.exe")
            root.destroy()
            
        def Products():
            os.startfile("Products.exe")
            root.destroy()

        self.transaction_records.pack(fill = BOTH, expand = 1)
        self.transaction_records.bind("<ButtonRelease-1>", TransactionInfo)
        #DisplayData()
        



#button widgets

        self.btnAdd = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Add", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = addData).grid(row = 1, column = 0, padx = 1)
        self.btnDelete = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Delete", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command=Delete).grid(row = 2, column = 0, padx = 1)
        self.btnReset = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Reset", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Reset).grid(row = 3, column = 0, padx = 1)
        self.btnSearch = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Search", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = SearchDB).grid(row = 4, column = 0, padx = 1)
        self.btnUpdate = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Update", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Update).grid(row = 5, column = 0, padx = 1)
        self.btnDisplay = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Display", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command= DisplayData).grid(row = 6, column = 0, padx = 1)
        self.btnCost = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Check Order", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Cost).grid(row = 7, column = 0, padx = 1)
        self.btnExit = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Exit", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Exit).grid(row = 8, column = 0, padx = 1)
        self.btnExpenses = Button(RightFrame3, font = ('times new roman', 20, 'bold'), text = "Expenses", bd = 1, pady = 1, padx = 10, width = 10, height = 3,bg = "#CEE5D0", command = Expenses).grid(row = 0, column = 0)
        self.btnProducts = Button(RightFrame3, font = ('times new roman', 20, 'bold'), text = "Products", bd = 1, pady = 1, padx = 10, width = 10, height = 3,bg = "#CEE5D0", command=Products).grid(row = 2, column = 0)
        self.btnCustomers = Button(RightFrame3, font = ('times new roman', 20, 'bold'), text = "Customers", bd = 1, pady = 1, padx = 10, width = 10, height = 3,bg = "#CEE5D0").grid(row = 4, column = 0)


if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()