import tkinter as tk
from tkinter import messagebox
import time
import os
import re


current_balance=10000000
count=0

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        '''here *args---used to pass a non key worder ,variable length argument list & it allows u to take in more argumetns than the formal argumetns'''
        '''kwargd---used to pass keyworded variable length argument list'''
        self.shared_data={"Balance":tk.IntVar()}
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, menupage,withdrawpage,depositpage,balancepage,withdraw_before_page,Resultframe,changepin,fundtransfer):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):#this page is for entering pin and account number.

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')#background color --black
        self.controller = controller
        self.controller.title('Lpu atm')#title of the atm
        self.controller.state('zoomed')#mode of the title.
        self.controller.iconphoto(False,tk.PhotoImage(file='lpu.png'))#icon of the project
        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=125)

        space_label=tk.Label(self,height=4,bg="black")#this is for space between logo and enter account no. box
        space_label.pack()


        password_label=tk.Label(self,text="Enter Your PIN",font=('arial',13,'bold'),bg="black",fg="white")#text of enter pin
        password_label.pack(pady=10)

        my_password=tk.StringVar()
        password_entry_box=tk.Entry(self,textvariable=my_password,font=('arial',12),width=20)#text box of pin
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):#func for to hide pin
            password_entry_box.configure(fg='black',show='*')
        password_entry_box.bind('<FocusIn>',handle_focus_in)

        
        def check_password():
            global count
            if len(my_password.get())==4:
                my_file=open(r"file.txt","r")
                disp=my_file.read()
                if my_password.get()==disp:
                    my_password.set('')#resets pin entry to empty
                    incorrect_password_label['text']=''
                    controller.show_frame('menupage')
                else:
                    messagebox.showwarning("Warning","The PIN is wrong")
                    count=count+1
                    incorrect_password_label['text']='Incorrect Credentials'
            else:
                 messagebox.showwarning("Warning","Invalid PIN..PIN should be 4 numericals")
                 count=count+1

            if(count==2):
                messagebox.showwarning("Warning","You are blocked. Try to enter after sometime")
                exit()
                

                


                
        enter_button=tk.Button(self,text="Enter",command=check_password,relief="raised",borderwidth=3,width=30,height=1)
        enter_button.pack(pady=10)

        incorrect_password_label=tk.Label(self,text='',font=('arial',13),fg='white',bg='#010203',anchor='n')
        incorrect_password_label.pack(fill='both',expand=True,pady=30)

        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')


        
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')


        tick()

class menupage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="black")
        self.controller = controller



        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=105)

        main_menu_label=tk.Label(self,text='Main Menu',font=('Arial',20,'bold'),fg='white',bg="black")

        main_menu_label.pack()
        selection_label = tk.Label(self,text='Choose an Option',font=('arial',20,'bold'),fg='white',bg='#682c03',anchor='w')
        selection_label.pack(fill='x')

        
        button_frame = tk.Frame(self,bg='#943404')
        button_frame.pack(fill='both',expand=True)


        #function for withdraw
        def withdraw():
            controller.show_frame("withdraw_before_page")


        #withdraw button on menu page
        withdraw_button=tk.Button(button_frame,text="Withdraw",command=withdraw,relief='raised',borderwidth=3,width=50,height=5)
        withdraw_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame("depositpage")


            
        deposit_button=tk.Button(button_frame,text="Deposit",command=deposit,relief='raised',borderwidth=3,width=50,height=5)
        deposit_button.grid(row=0,column=1,pady=50)


        def balance():
            controller.show_frame("balancepage")


            
        balance_button=tk.Button(button_frame,text="Balance Enquiry",command=balance,relief='raised',borderwidth=3,width=50,height=5)
        balance_button.grid(row=1,column=0,pady=50)


        def fundtransfer():
            controller.show_frame("fundtransfer")


            
        fundtransfer_button=tk.Button(button_frame,text="Fund Transfer",command=fundtransfer,relief='raised',borderwidth=3,width=50,height=5)
        fundtransfer_button.grid(row=1,column=1,pady=50,padx=1190)


        def changepin():
            controller.show_frame("changepin")


            
        changepin_button=tk.Button(button_frame,text="Change Pin",command=changepin,relief='raised',borderwidth=3,width=50,height=5)
        changepin_button.grid(row=2,column=0,pady=50)



        
        def Exit():
            controller.show_frame('StartPage')


            
        exit_button=tk.Button(button_frame,text="Exit",command=Exit,relief='raised',borderwidth=3,width=50,height=5)
        exit_button.grid(row=2,column=1,pady=50)


        


        #bottom logos 
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')


        tick()

       
class withdraw_before_page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="black")
        self.controller = controller

        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#3d3d5c')
        heading_label.pack(pady=105)
        button_frame=tk.Frame(self,bg='#943404')
        button_frame.pack(fill='both',expand=True)

        selection_label = tk.Label(self,text='Choose an Option',font=('arial',20,'bold'),fg='white',bg='#3d3d5c',anchor='w')
        selection_label.pack(fill='x')


        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')

        tick()


        def savingswithdraw():
            controller.show_frame("withdrawpage")
        def currentwithdraw():
            controller.show_frame("withdrawpage")


            
        deposit_button=tk.Button(button_frame,text="Savings Account",command=savingswithdraw,relief='raised',borderwidth=3,width=50,height=5)
        deposit_button.grid(row=0,column=0,pady=50)

        deposit_button=tk.Button(button_frame,text="Current Account",command=currentwithdraw,relief='raised',borderwidth=3,width=50,height=5)
        deposit_button.grid(row=0,column=1,pady=50,padx=1190)
        

class withdrawpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="black")
        self.controller = controller

        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='orange')
        heading_label.pack(pady=105)

        choose_amount_label=tk.Label(self,text='Enter amount you want to withdraw',font=('Arial',20,'bold'),fg='white',bg="black")

        choose_amount_label.pack(pady=50)

        button_frame=tk.Frame(self,bg='#943404')
        button_frame.pack(fill='both',expand=True)

        def withdraw(_):
            global current_balance
            if(current_balance>cash.get()):
                current_balance-=int(cash.get())
                controller.shared_data['Balance'].set(current_balance)
                cash.set('')
                messagebox.showinfo("RESULT","TRANSACTION SUCCESSFUL")
                controller.show_frame('Resultframe')
            else:
                messagebox.showerror("Error","INSUFFICIENT FUNDS")
                cash.set('')
            
        cash=tk.IntVar()
        amount_entry=tk.Entry(button_frame,textvariable=cash,width=30)
        amount_entry.pack(ipady=7,pady=20)

        amount_entry.bind('<Return>',withdraw)


        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')


        tick()

class Resultframe(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=125)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)

        result_text=tk.Label(self,text='Transaction is Successful',font=('arial',15,'bold'),foreground='white',background='black')

        result_text.pack(pady=10)
        
        result_text2=tk.Label(self,text="What would you like to do next?",font=('arial',12),fg='white',bg='black')
        result_text2.pack(pady=10)

        button_frame=tk.Frame(self,relief='raised',bg='#ed7014')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('menupage')
        menu_button=tk.Button(button_frame,command=menu,text='Menu',relief='raised',width=50,height=3,borderwidth=3)
        menu_button.grid(row=0,column=0,pady=5)


        def exit():
            messagebox.askquestion("CONFIRMATION","ARE YOU SURE?")
            controller.show_frame('StartPage')
        exit_button=tk.Button(button_frame,text='EXIT',command=exit,relief='raised',borderwidth=3,width=50,height=3)
        exit_button.grid(row=0,column=1,pady=5,padx=1190)
        
        
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')


        tick()

class depositpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller


        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=125)

        space_label=tk.Label(self,height=4,bg="black")#this is for space between logo and enter account no. box
        space_label.pack()


        Enter_amount_label=tk.Label(self,text="Enter Amount to deposit",font=('arial',13,'bold'),bg="black",fg="white")
        Enter_amount_label.pack(pady=10)

        cash=tk.IntVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=('arial',13),width=22)
        deposit_entry.pack(ipady=7)


        def deposit_cash():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data["Balance"].set(current_balance)
            messagebox.showinfo("Result","Deposit is succesful")
            controller.show_frame('Resultframe')
            cash.set('')

        enter_button=tk.Button(self,text='ENTER',command=deposit_cash,relief='raised',borderwidth=3,width=20,height=3)
        enter_button.pack(pady=10)

        two_tone_label=tk.Label(self,bg="#33334d")
        two_tone_label.pack(fill='both',expand=True)
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')


        tick()



class balancepage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=125)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)

        balance_text=tk.Label(self,text='Available Balance in your account',font=('arial',15,'bold'),foreground='white',background='#ed7014')

        balance_text.pack()
        
        balance_label=tk.Label(self,textvariable=controller.shared_data['Balance'],font=('arial',13))

        balance_label.pack(ipady=7,pady=10)

        button_frame=tk.Frame(self,relief='raised',bg='#ed7014')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('menupage')
        menu_button=tk.Button(button_frame,command=menu,text='Menu',relief='raised',width=50,height=3,borderwidth=3)
        menu_button.grid(row=0,column=0,pady=5)


        def exit():
            controller.show_frame('StartPage')
        exit_button=tk.Button(button_frame,text='EXIT',command=exit,relief='raised',borderwidth=3,width=50,height=3)
        exit_button.grid(row=0,column=1,pady=5,padx=1190)
        
        
        bottom_frame=tk.Frame(self,relief='raised',borderwidth=3)
        bottom_frame.pack(fill='x',side='bottom')
        visa_photo=tk.PhotoImage(file='visa.png')
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side='left')
        visa_label.image=visa_photo


        mastercard_photo=tk.PhotoImage(file='mastercard.png')
        mastercard_label=tk.Label(bottom_frame,image=mastercard_photo)
        mastercard_label.pack(side='left')
        mastercard_label.image=mastercard_photo


        rupay_photo=tk.PhotoImage(file='rupay.png')
        rupay_label=tk.Label(bottom_frame,image=rupay_photo)
        rupay_label.pack(side='left')
        rupay_label.image=rupay_photo


        def tick():
            current_time=time.strftime('%I:%M %p')
            time_label.config(text=current_time)
            time_label.after(200,tick)
            
        time_label=tk.Label(bottom_frame,font=('arial',14))
        time_label.pack(side='right')


        tick()

class changepin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=125)

        space_label=tk.Label(self,height=4,bg="black")#this is for space between logo and enter account no. box
        space_label.pack()


        Enter_pin_label=tk.Label(self,text="Enter New PIN",font=('arial',13,'bold'),bg="black",fg="white")
        Enter_pin_label.pack(pady=10)

        newpin=tk.StringVar()
        pin_entry=tk.Entry(self,textvariable=newpin,font=('arial',13),width=22)
        pin_entry.pack(ipady=7)

        def handle_focus_in(_):
            pin_entry.configure(fg='black',show='*')
        pin_entry.bind('<FocusIn>',handle_focus_in)

        def pinchange():
            file=open(r"file.txt","w")
            file.write(newpin.get())
            file.close()
            messagebox.showinfo("Result","PIN changed successfully")
            #pin_entry.set('')
            controller.show_frame('Resultframe')
            
        submit_pin_button=tk.Button(self,text='Change',command=pinchange,relief='raised',borderwidth=2,width=20,height=1)
        submit_pin_button.pack(ipady=7,pady=10)

class fundtransfer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='black')
        self.controller = controller
        heading_label=tk.Label(self,text='LPU ATM',font=('arial',50,'bold'),foreground='white',background='#ed7014')
        heading_label.pack(pady=125)

        account_num_label=tk.Label(self,text="Enter Account number of receiver",font=('arial',16),fg='white',bg='black')
        account_num_label.pack()

        account_num=tk.IntVar()
        
        account_num_entry=tk.Entry(self,textvariable=account_num,font=('arial',13),width=22)
        account_num_entry.pack(pady=15)

        amount_entry_label=tk.Label(self,text="Enter Amount you want to send",font=('arial',16),fg='white',bg='black')
        amount_entry_label.pack(pady=15)

        amount_fund_transfer=tk.IntVar()
        amount_entry=tk.Entry(self,textvariable=amount_fund_transfer,font=('arial',13),width=22)
        amount_entry.pack(pady=10)

        def fundtransfer():
            global current_balance
            account_num_get=int(account_num.get())
            if(current_balance>amount_fund_transfer.get()):
                current_balance-=int(amount_fund_transfer.get())
                controller.shared_data['Balance'].set(current_balance)
                amount_fund_transfer.set('')
                messagebox.showinfo("RESULT","TRANSACTION SUCCESSFUL")
                controller.show_frame('Resultframe')
                account_num.set('')
            else:
                messagebox.showerror("Error","INSUFFICIENT FUNDS")
                amount_fund_transfer.set('')
        button_fund_transfer=tk.Button(self,text='SEND',command=fundtransfer,relief='raised',borderwidth=2,width=20,height=1)
        button_fund_transfer.pack(ipady=7,pady=10)






if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
