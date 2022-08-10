from guizero import App, Text, TextBox, Slider, PushButton, Window, Box

def main():
    app = App(title="Company Name", layout="grid")
    User = Text(app, text="User ID: ", size=20, grid=[0, 0], align="left")
    User_Box = TextBox(app, grid=[1, 0], align="left", width="fill")
    Master_Pass = Text(app, text="Master Password: ", grid=[0, 1], size=20, align="left")
    Pass_Box = TextBox(app, align="left", grid=[1, 1], width="fill")
    Login = PushButton(app, text="Login", grid=[0, 2], align="left", width=5, height=2)
    Blank = Text(app, text="        ", grid=[0, 5], align="left", size=20)
    Welcome = Text(app, text="New to Company? Welcome, sign up below:", grid=[0, 6], align="left", size=15)
    Sign_Up = PushButton(app, text="Sign Up", grid=[0, 8], width=5, height=2, align="left")

    app.display()
if __name__ == '__main__':
    main()

