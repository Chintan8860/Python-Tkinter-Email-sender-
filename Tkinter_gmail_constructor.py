from tkinter import *
from tkinter.messagebox import showinfo, showerror
import smtplib
class Login(Tk):
    def __init__(self):
        try:
            self.gmail = smtplib.SMTP("smtp.gmail.com", 587)
        except Exception as e:
            showerror("Fatal Error", str(e))
            exit()
        Tk.__init__(self)
        self.geometry("1920x1080")
        self.title("e-Sender")
        self.config(bg="#E29484")
        me = StringVar()
        mp = StringVar()
        def spaccing():
            Label(self, text=" ", bg="#E29484").pack()
        spaccing()
        spaccing()
        Label(self,text="email sending system", bg="black", fg="white", width="100", height="2", font=("Calibri", 13)).pack()
        spaccing()
        Label(self, text="Your Gmail account:", bg="#E29484",font=("calibri",13)).pack()
        self.my_email = Entry(self, textvariable=me, width=50)
        self.my_email.pack()
        spaccing()
        Label(self, text="Your Password:",  bg="#E29484",font=("calibri",13)).pack()
        self.my_passw = Entry(self, textvariable=mp, width=50, show='X')
        self.my_passw.pack()
        spaccing()
        self.email_button = Button(self, text="Process to sending mail", width="50", height="4", command=self.login_gmail)
        self.email_button.pack()
    def login_gmail(self):
        account = self.my_email.get()
        self.password = self.my_passw.get()
        self.gmail.ehlo()
        self.gmail.starttls()
        self.gmail.login(account, self.password)
        self.gmail.login(account, self.password)

        try:
            self.gmail.login(account, self.password)
            showinfo("Success", "You successfully login \n press ok for sending mail ")
        except:
            showerror("Error", "Enter a Currect id & password ")
            exit()
        gmail = self.gmail
        newEmail(gmail, account)
        self.withdraw()
class newEmail(Login):
    def __init__(self, gmail, account):
        Tk.__init__(self)
        self.title("New Email")
        self.geometry('900x700')
        self.config(bg="#9B9999")
        self.gmail = gmail
        self.email = account
        et = StringVar()
        es = StringVar()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text="From: %s" % account, font=("Calibri", 15)).pack()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text="To:", bg="#9B9999",font=("Calibri", 13)).pack()
        self.email_to = Entry(self, textvariable=et, width=50)
        self.email_to.pack()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text="Subject:", bg="#9B9999", font=("Calibri", 13)).pack()
        self.email_subject = Entry(self, textvariable=es, width=50)
        self.email_subject.pack()
        Label(self, text=" ", bg="#9B9999").pack()
        Label(self, text="Your Message:", bg="#9B9999",font=("Calibri", 13)).pack()
        self.email_msg = Text(self, width=50, height=15)
        self.email_msg.pack()
        Label(self, text=" ", bg="#9B9999").pack()
        self.email_button = Button(self, text="Send mail", command=self.sendEmail,width="50", height="4")
        self.email_button.pack(side=TOP)
    def sendEmail(self):
        self.to = self.email_to.get()
        self.subject = self.email_subject.get()
        self.msg = self.email_msg.get("1.0", END)
        headers = "From: %s\nTo: %s\nSubject: %s\n\n" % (self.email, self.to, self.subject)
        body = str(headers + self.msg)
        try:
            self.gmail.sendmail(self.email, self.to, body)
            showinfo("Completed", "Email sent successfully to %s..." % self.to)
        except Exception as e:
            showerror("Somthing was Wrong!!!", str(e))
            exit()
L = Login()
L.mainloop()
