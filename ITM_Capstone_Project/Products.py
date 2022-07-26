from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import os

class ConnectorDB:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(0 * titlespace + "Sample Business GUI")
        self.root.geometry("1325x595+100+0")
        self.root.resizable(width = False, height = False)

        #==========================Frame Design=========================================
      
        MainFrame = Frame(self.root, bd =10, width = 1900, height = 700, relief = RIDGE, bg = '#ECB390')
        MainFrame.grid()

        titlespace = Frame(MainFrame, bd = 7, width = 800, height = 200,padx = 2, relief = RIDGE,bg = '#FCF8E8')
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
        #==========================Variables Declaration=========================================

        Prod_ID = StringVar()
        Prod_Name = StringVar()
        Prod_Price = StringVar()

        #========================Functions Declaration=========================================

#exits the window
        def iExit():
            iExit = tkinter.messagebox.askyesno("Sample Business GUI", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
#resets the text on the entry widgets
        def Reset():
            self.entProd_ID.delete(0, END)
            self.entProd_Name.delete(0, END)
            self.entProd_Price.delete(0, END)
#clears the items on the treeview widget
        def clear_all():
            for item in self.product_records.get_children():
                self.product_records.delete(item)
#adds new data to the database
        def addData():
            if Prod_ID.get() =="" or Prod_Name.get() =="" or Prod_Price.get() =="":
                tkinter.messagebox.askyesno("Sample Business GUI", "Enter Correct Details")
            else:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("insert into products values(%s,%s,%s)", (

                Prod_ID.get(),
                Prod_Name.get(),
                Prod_Price.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Sample Business GUI", "Record Entered Successfully")
#displays the data of the database
        def DisplayData():
                clear_all()
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("select * from products")
                result = cur.fetchall()
                if len(result) != 0:
                    self.product_records.delete(*self.product_records.get_children())
                    for row in result:
                        self.product_records.insert('', END, values = row)
                    sqlCon.commit()
                sqlCon.close()
#allows the user to see their selected item in the treeview in their entry widgets
        def ProductInfo(ev):
            viewInfo = self.product_records.focus()
            learnerData = self.product_records.item(viewInfo)
            row = learnerData['values']
            Prod_ID.set(row[0]),
            Prod_Name.set(row[1]),
            Prod_Price.set(row[2])
#Updates an item in the database
        def Update():
            try:
                sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                cur = sqlCon.cursor()
                cur.execute("update products set product_name = %s, product_price = %s where product_id = %s", (

                Prod_Name.get(),
                Prod_Price.get(),
                Prod_ID.get()
                ))
                sqlCon.commit()
                sqlCon.close()
                tkinter.messagebox.showinfo("Sample Business GUI", "Record Updated Successfully")
                Reset()
            except:
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()
#deletes an item in the database
        def DeleteDB():
            try:
                if Prod_ID.get() =="":
                    tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                    Reset()
                else:
                    sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                    cur = sqlCon.cursor()
                    cur.execute("delete from products where product_id = %s", Prod_ID.get())

                    sqlCon.commit()
                    sqlCon.close()
                    tkinter.messagebox.showinfo("Sample Business GUI", "Record Deleted Successfully")
                    Reset()
            except:
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()

        
  #searches for an item in the database      
        def SearchDB():
            try:
                if Prod_ID.get() =="":
                    tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                    Reset()
                else:
                    sqlCon = pymysql.connect(host = "localhost", user = "sampleuser", password = "password", database = "newbusiness")
                    cur = sqlCon.cursor()
                    cur.execute("select * from products where product_id =%s"%Prod_ID.get())

                    row = cur.fetchone()
                
                    Prod_ID.set(row[0]),
                    Prod_Name.set(row[1]),
                    Prod_Price.set(row[2])
                
                    sqlCon.commit() 
                    sqlCon.close()
            except:   
                tkinter.messagebox.showinfo("Sample Business GUI", "No Such Record Found")
                Reset()
#transfers to the customers window
        def Customers():
            os.startfile("Customers.exe")
            root.destroy()
#transfers to the expenses window
        def Expenses():
            os.startfile("Expenses.exe")
            root.destroy()
            
        #================================================Label Title==========================================================

        self.lbtitle = Label(titlespace, font = ('times new roman', 40, 'bold'), text = "Product Database", bd = 5,bg = '#FCF8E8')
        self.lbtitle.grid(row = 0, column = 0, padx = 200)
        
        #================================================Label and Entry Widget==========================================================
        
        self.lblProd_ID = Label(RightFrame1, font = ('times new roman', 12, 'bold'), text = "Product ID", bd = 7,bg = '#FCF8E8')
        self.lblProd_ID.grid(row = 0, column = 0, sticky = W, padx = 100)
        self.entProd_ID = Entry(RightFrame1, font = ('times new roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Prod_ID)
        self.entProd_ID.grid(row = 0, column = 1, sticky = W, padx = 100)
        
        self.lblProd_Name = Label(RightFrame1, font = ('times new roman', 12, 'bold'), text = "Product Name", bd = 7,bg = '#FCF8E8')
        self.lblProd_Name.grid(row = 1, column = 0, sticky = W, padx = 100)
        self.entProd_Name = Entry(RightFrame1, font = ('times new roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Prod_Name)
        self.entProd_Name.grid(row = 1, column = 1, sticky = W, padx = 100)        

        self.lblProd_Price = Label(RightFrame1, font = ('times new roman', 12, 'bold'), text = "Product Price", bd = 7,bg = '#FCF8E8')
        self.lblProd_Price.grid(row = 2, column = 0, sticky = W, padx = 100)
        self.entProd_Price = Entry(RightFrame1, font = ('times new roman', 12, 'bold'), bd = 5, width = 44, justify = 'left', textvariable = Prod_Price)
        self.entProd_Price.grid(row = 2, column = 1, sticky = W, padx = 100)

        #=======================================================Table Treeview Widget=============================================================

        scroll_y = Scrollbar(RightFrame, orient = VERTICAL)
        
        self.product_records = ttk.Treeview(RightFrame, height = 14, columns = ("Prod_ID", "Prod_Name", "Prod_Price"), yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT, fill = Y)
        
        self.product_records.heading("Prod_ID", text="Product ID")
        self.product_records.heading("Prod_Name", text="Product Name")
        self.product_records.heading("Prod_Price", text="Product Price")

        self.product_records['show'] = 'headings'

        self.product_records.column("Prod_ID", width = 100)
        self.product_records.column("Prod_Name", width = 100)
        self.product_records.column("Prod_Price", width = 100)

        self.product_records.pack(fill = BOTH, expand = 1)
        self.product_records.bind("<ButtonRelease-1>", ProductInfo)
        #DisplayData()
        
        
        #=======================================================Buttons Widget===================================================================

        self.btnAdd = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Add", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = addData).grid(row = 1, column = 0, padx = 1)
        
        self.btnDelete = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Delete", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = DeleteDB).grid(row = 2, column = 0, padx = 1)
        
        self.btnReset = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Reset", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Reset).grid(row = 3, column = 0, padx = 1)
        
        self.btnSearch = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Search", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0", command =SearchDB).grid(row = 4, column = 0, padx = 1)
        
        self.btnDisplay = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Display", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = DisplayData).grid(row = 5, column = 0, padx = 1)

        self.btnUpdate = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Update", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = Update).grid(row = 6, column = 0, padx = 1)

        self.btnExit = Button(LeftFrame2, font = ('times new roman', 16, 'bold'), text = "Exit", bd = 1, pady = 1, padx = 10, width = 8, height = 2,bg = "#CEE5D0",command = iExit).grid(row = 7, column = 0, padx = 1)
        
        self.btnExpenses = Button(RightFrame3, font = ('times new roman', 20, 'bold'), text = "Expenses", bd = 1, pady = 1, padx = 10, width = 10, height = 3,bg = "#CEE5D0",command = Expenses).grid(row = 0, column = 0)
        
        self.btnProducts = Button(RightFrame3, font = ('times new roman', 20, 'bold'), text = "Products", bd = 1, pady = 1, padx = 10, width = 10, height = 3,bg = "#CEE5D0").grid(row = 2, column = 0)
        
        self.btnCustomers = Button(RightFrame3, font = ('times new roman', 20, 'bold'), text = "Customers", bd = 1, pady = 1, padx = 10, width = 10, height = 3,bg = "#CEE5D0",command = Customers).grid(row = 4, column = 0)
        
if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()