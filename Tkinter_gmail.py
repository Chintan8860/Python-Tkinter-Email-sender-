import smtplib
from tkinter import *
def spacing():
    Label(text=" ",bg="#E29484").pack()
    Label(text=" ",bg="#E29484").pack()
def main_page():
    global screen
    screen = Tk()
    screen.title("Gmail  System")
    screen.geometry('1920x1080')
    spacing()
    spacing()
    screen.configure(bg="#E29484")
    Label(text="email sending system", bg="black", fg="white", width="100", height="2", font=("Calibri", 13)).pack()
    spacing()
    icon = PhotoImage(file="3.png")
    Label(screen, image=icon,bg="#E29484").pack(padx=50,pady=20)
    global gmail_id
    global recive_email_id
    global password
    password = StringVar()
    gmail_id = StringVar()
    recive_email_id = StringVar()
    Label(text="enter a sender gmail id",font=("calibri",13),bg="#E29484").pack()
    id=Entry(screen, textvariable=gmail_id, width="50")
    id.pack()
    Label(text=" ",bg="#E29484").pack()
    Label(text="enter sender mail password",font=("calibri",13),bg="#E29484").pack()
    id = Entry(screen, textvariable=password,  show='X',width="50")
    id.pack()
    Label(text=" ",bg="#E29484").pack()
    Label(text="enter a reciver email id",font=("calibri",13),bg="#E29484").pack()
    id = Entry(screen, textvariable=recive_email_id, width="50")
    id.pack()
    spacing()
    Button(text="Process to sending mail", width="50", height="4",command=body).pack()
    screen.mainloop()
def body():
    global b_screen
    global sub_mail
    global tx
    sub_mail = StringVar()
    tx = StringVar()
    b_screen = Toplevel(screen)
    b_screen.configure(bg="#9B9999")
    b_screen.title("body page")
    b_screen.geometry('900x700')
    Label(b_screen,text=" ",bg="#9B9999").pack()
    Label(b_screen,text=" ",bg="#9B9999").pack()
    Label(b_screen,text="enter a body part and subject for email", bg="black", fg="white", width="100", height="2", font=("Calibri", 13)).pack()
    Label(b_screen,text=" ",bg="#9B9999").pack()
    Label(b_screen,text=" ",bg="#9B9999").pack()
    Label(b_screen,text="enter a mail subject",font=("calibri",13),bg="#9B9999").pack()
    sub = Entry(b_screen, textvariable=sub_mail, width="50")
    sub.pack()
    Label(b_screen,text=" ",bg="#9B9999").pack()
    Label(b_screen,text="enter a mail body (content)",font=("calibri",13),bg="#9B9999").pack()
    global txt
    txt = Text(b_screen, width=50, height=15)
    txt.pack()
    global content
    content = txt.get(1.0, END)
    Label(b_screen,text=" ",bg="#9B9999").pack()
    Label(b_screen,text=" ",bg="#9B9999").pack()
    photo = PhotoImage(file=r"4.png")
    photoimage = photo.subsample(1, 1)
    Button(b_screen,text="Send email ", width="300", height="70",command=activity,image =photoimage,compound = RIGHT).pack(side=TOP)
    b_screen.mainloop()
def activity():
    gmail_email=gmail_id.get()
    gmail_passwod=password.get()
    recevie_email=recive_email_id.get()
    subject_mail=sub_mail.get()
    body_mail =  txt.get(1.0, END)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(gmail_email, gmail_passwod)
    headers = "\r\n".join(["from: " + gmail_email,
                               "subject: " + subject_mail,
                               "to: " + recevie_email,
                               "mime-version: 1.0",
                               "content-type: text/html"])
    content = headers + "\r\n\r\n" + body_mail
    s.sendmail(gmail_email,recevie_email, content)
    Label(b_screen, text="Successfully send .....!!!!!", fg="green",bg="#9B9999").pack()
    s.quit()
main_page()
