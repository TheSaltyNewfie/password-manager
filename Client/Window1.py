from guizero import App, Text, TextBox, PushButton, Window, error
import random

##  Open and close windows  ##

def open_window():
    Window.show(sign_up_window)

def open_Vault():
    Window.show(Vault_window)

def closed_window():
    Window.hide(sign_up_window)

def open_Password():
    Window.show(Password_window)

def close_Password():
    Window.hide(Password_window)

def logging_off():
    Window.hide(Vault_window)
    Window.hide(sign_up_window)


##  Window 1  ##

app = App(title="Company Name", layout="grid")

sign_up_window = Window(app, title="Sign Up", layout="grid")
sign_up_window.hide()

Vault_window = Window(app, title="My Passwords", layout="grid")
Vault_window.hide()

Password_window = Window(app, title="New Password", layout="grid")
Password_window.hide()

##  Login  ##

User = Text(app, text="User ID: ", size=20, grid=[0, 0], align="left")
User_Box = TextBox(app, grid=[1, 0], align="left", width="fill")

Master_Pass = Text(app, text="Master Password: ", grid=[0, 1], size=20, align="left")
Pass_Box = TextBox(app, align="left", grid=[1, 1], width="fill", hide_text=True)

Login = PushButton(app, text="Login", grid=[0, 2], align="left", width=5, height=2)


Blank = Text(app, text="        ", grid=[0, 5], align="left", size=20)


##  Create Account  ##

Welcome = Text(app, text="New to Company? Welcome, sign up below:", grid=[0, 6], align="left", size=15)
Sign_Up = PushButton(app, text="Sign Up", grid=[0, 8], width=5, height=2, align="left", command=open_window)


##  Window 2  ##

New_User = Text(sign_up_window, text="User ID: ", size=20, grid=[0, 0], align="left")
New_UserBox = TextBox(sign_up_window, grid=[1, 0], align="left", width="fill")

New_Pass = Text(sign_up_window, text="Master Password: ", grid=[0, 1], size=20, align="left")
New_PassBox = TextBox(sign_up_window, align="left", grid=[1, 1], width="fill", hide_text=True)


Confirm_Pass = Text(sign_up_window, text="Confirm Password: ", grid=[0, 3], size=20, align="left")
Confirm_PassBox = TextBox(sign_up_window, align="left", grid=[1, 3], width="fill", hide_text=True)


def confirm_button():
    def match():
        sign_up_window.warn("Uh oh!", "Your answers don't seem to match.")

    def no_username():
        sign_up_window.warn("Uh oh!", "Please fill in all boxes.")

    def too_short():
        sign_up_window.warn("Uh oh!", "Please enter a password that is 12 characters.")

    def correct_password():
        open_Vault()

    if len(New_UserBox.value) == 0 or len(New_PassBox.value) == 0 or len(Confirm_PassBox.value) == 0:
        Confirm.when_clicked = no_username()
    elif len(New_PassBox.value) < 12 or len(Confirm_PassBox.value) < 12:
        Confirm.when_clicked = too_short()
    else:
        if New_PassBox.value != Confirm_PassBox.value:
            Confirm.when_clicked = match()
        elif New_PassBox.value == Confirm_PassBox.value:
            Confirm.when_clicked = correct_password()


Back = PushButton(sign_up_window, text="Back", align="bottom", grid=[2,0], command=closed_window)
Confirm = PushButton(sign_up_window, text="Confirm", align="right", grid=[2,1],command=confirm_button)


##  Window 3  ##

Blank_Button = PushButton(Vault_window, text="    Saved Passwords     ", grid=[0, 0], width=40)
Plus_password = PushButton(Vault_window, text="+", grid=[5, 0], command=open_Password)

Logout = PushButton(Vault_window, text="Log Out", grid=[5, 5], command=logging_off)

Plus_password.when_clicked = open_Password()


##  Window 4  ##

Password_Name = Text(Password_window, text="Title: ", size=20, grid=[0, 0], align="left")
Name_TextBox = TextBox(Password_window, grid=[1, 0], width="fill", align="left")

Password_Username = Text(Password_window, text="Username/Email: ", size=20, grid=[0, 1], align="left")
Username_TextBox = TextBox(Password_window, grid=[1, 1], width="fill", align="left")

Password_Pass = Text(Password_window, text="Password: ", size=20, grid=[0, 2], align="left")
Password_TextBox = TextBox(Password_window, grid=[1, 2], width="fill", align="left")

Password_Blank = Text(Password_window, text="                  ", size=20, grid=[0, 3], width="fill")

Exit_Button = PushButton(Password_window, text="Back", height=1, width=2, grid=[0, 8], align="left", command=close_Password)
Save_Button = PushButton(Password_window, text="Save", height=1, width=2, grid=[1, 8])

Password_Text = Text(Password_window, text="To generate a password: ", size=15, grid=[0, 4], align="left")
Password_Cont = Text(Password_window, text="Enter preferred number of characters.", size=15, grid=[0, 5], align="left")
Password_Length = TextBox(Password_window, grid=[1, 5], align="left", width=2, height=1)

def get_passwords():
    password_possibilities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,./?!@#$%&(){}1234567890"

    length = int(len(Password_Length.value))

    for c in range(length):
        password = ''
        password += random.choice(password_possibilities)
        password = str(password)
        printpass = TextBox(Password_window, text=password, width=20, height=10, grid=[0,10], visible=True, multiline=True)


Generate = PushButton(Password_window, command=get_passwords, text="Generate", grid=[1, 7])

app.display()
