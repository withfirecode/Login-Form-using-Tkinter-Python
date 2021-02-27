from tkinter import *
import tkinter.messagebox as MessageBox

root = Tk()
root.title("Login System")
root.geometry("600x330")
root.configure(bg="#990033")
root.iconbitmap("Login1.ico")

#Validate Function
def validate():
    UserVal = UserEntry.get()
    PassVal = PassEntry.get()

    if UserVal == "withfirecode" and PassVal == "Pune1234":
        MessageBox.showinfo(UserVal, "Logged Successfully!")
    else:
        MessageBox.showinfo(UserVal, "Wrong Credential")

#Labels

TitleLabel = Label(root, text="LOGIN SYSTEM",fg="white",bg="#990033", font = ("Segoe UI Black",23,"bold"))
TitleLabel.place(x=190, y=50)

UserLabel = Label(root, text="User Name : ",fg="white",bg="#990033", font=("Segoe UI Black",15))
UserLabel.place(x=150, y=120)

PassLabel = Label(root, text=" Password  : ",fg="white",bg="#990033", font=("Segoe UI Black",15))
PassLabel.place(x=150, y=170)

#EntryBox

UserEntry = Entry(root, borderwidth=3)
UserEntry.place(x=330, y=130)

PassEntry = Entry(root, borderwidth=3)
PassEntry.place(x=330, y=180)

#Button

Submit = Button(root, text="Login", bg="#4d0019", fg="white", font=("Segoe UI Black",13), command=validate)
Submit.place(x=275, y=240)



root.mainloop()






