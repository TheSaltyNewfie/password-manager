from guizero import App, Text, TextBox, Slider, PushButton, Window, Box

##  Open and close windows  ##

def open_window():
    Window.show(sign_up_window)

def open_Vault():
    Window.show(Vault_window)

def closed_window():
    Window.hide(sign_up_window)


##  Window 1  ##

app = App(title="Company Name", layout="grid")

##  Login  ##

User = Text(app, text="User ID: ", size=20, grid=[0, 0], align="left")
User_Box = TextBox(app, grid=[1, 0], align="left", width="fill")

Master_Pass = Text(app, text="Master Password: ", grid=[0, 1], size=20, align="left")
Pass_Box = TextBox(app, align="left", grid=[1, 1], width="fill")

Login = PushButton(app, text="Login", grid=[0, 2], align="left", width=5, height=2)

# if (password_check(passwd)):
#     print("Password is valid")
# else:
#     print("Invalid Password !!")

Blank = Text(app, text="        ", grid=[0, 5], align="left", size=20)


##  Create Account  ##

Welcome = Text(app, text="New to Company? Welcome, sign up below:", grid=[0, 6], align="left", size=15)
Sign_Up = PushButton(app, text="Sign Up", grid=[0, 8], width=5, height=2, align="left", command=open_window)


##  Window 2  ##

sign_up_window = Window(app, title="Sign Up", layout="grid")
sign_up_window.hide()

New_User = Text(sign_up_window, text="User ID: ", size=20, grid=[0, 0], align="left")
New_UserBox = TextBox(sign_up_window, grid=[1, 0], align="left", width="fill")

New_Pass = Text(sign_up_window, text="Master Password: ", grid=[0, 1], size=20, align="left")
New_PassBox = TextBox(sign_up_window, align="left", grid=[1, 1], width="fill")

Password_Length = Text(sign_up_window, text="Password Strength", grid=[0, 2], align="left")

# Checker = Password_Length.value
# def password_check(Checker):


Confirm_Pass = Text(sign_up_window, text="Confirm Password: ", grid=[0, 3], size=20, align="left")
Confirm_PassBox = TextBox(sign_up_window, align="left", grid=[1, 3], width="fill")


Vault_window = Window(app, title="My Passwords", layout="grid")
Vault_window.hide()


def confirm_button():
    def match():
        sign_up_window.warn("Uh oh!", "Your answers don't seem to match.")

    def no_username():
        sign_up_window.warn("Uh oh!", "Please fill in all boxes.")

    def correct_password():
        open_Vault()

    if len(New_UserBox.value) == 0 or len(New_PassBox.value) == 0 or len(Confirm_PassBox.value) == 0:
        Confirm.when_clicked = no_username()
    else:
        if New_PassBox.value == Confirm_PassBox.value:
            Confirm.when_clicked = correct_password()
        elif New_PassBox.value != Confirm_PassBox.value:
            Confirm.when_clicked = match()


Back = PushButton(sign_up_window, text="Back", align="bottom", grid=[2,0], command=closed_window)
Confirm = PushButton(sign_up_window, text="Confirm", align="right", grid=[2,1],command=confirm_button)


##  Window 3  ##


app.display()
