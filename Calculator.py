# Pay Calculator GUI Application written using Python
# Python Version 3.7.9

from tkinter import *
import tkinter.messagebox


class payGUI:

    def __init__(self, master):
        self.container = Frame(master)
        self.container.grid()

        self.payperhour = StringVar()
        self.workhrs = StringVar()

        self.l1 = Label(
            self.container, text="Welcome to the Pay Roll Calculator", fg='blue').grid(row=0, column=0, columnspan=2, padx = 5, pady = 10)
        self.l2 = Label(
            self.container, text="Please Enter your hourly rate :").grid(row=1, column=0 , padx = 5, pady = 5)
        self.l3 = Label(
            self.container, text="Numbers of workhrs Worked :").grid(row=2, column=0, padx = 5, pady = 5)

        self.mypayperhour = Entry(
            self.container, textvariable=self.payperhour).grid(row=1, column=1)
        self.myworkhrs = Entry(
            self.container, textvariable=self.workhrs).grid(row=2, column=1)

        self.mybutton1 = Button(self.container, text='Calculate Pay')
        self.mybutton1.grid(row=3, column=0, columnspan=2, )
        self.mybutton1.bind("<Button-1>", self.calculatePayRoll)
        self.l4 = Label(
            self.container, text="Made by blue-1ms 2020", fg='blue').grid(row=5, column=0, columnspan=2, padx = 5, pady = 50)


    def calculatePayRoll(self, event):
        try:
            self.h = float(self.workhrs.get())
            self.hs = float(self.payperhour.get())
            self.salary = self.h*self.hs
            self.labelresult = Label(
                self.container, text="Your salary is: $ %.2f" % self.salary).grid(row=4, column=0, columnspan=2)
        except ValueError:
            tkinter.messagebox.showinfo(
                "Invalid Value", "Please Input the using correct value.")


wageGUI = Tk()
wageGUI.iconphoto(False, tkinter.PhotoImage(file='wage.png'))
wageGUI.geometry('315x200+500+200')
wageGUI.title('Pay Roll Calculator')
payGUI = payGUI(wageGUI)

wageGUI.mainloop()
