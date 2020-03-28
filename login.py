# Imports 

from tkinter import* 
from tkinter import ttk

class kq: 

    user = 'kevin'
    password = 'quinn'

    def __init__(self, root):

        self.root = root 
        self.root.title('Login Screen')

        Label(text = 'Username ', font = 'Helvetica 15').grid(row = 1, column = 1, pady = 20)
        self.username = Entry()
        self.username.grid(row = 1, column = 2, columnspan = 10)

        Label(text = 'Password ', font = 'Helvetica 15').grid(row = 2, column = 1, pady = 20)
        self.password = Entry(show = '*')
        self.password.grid(row = 2, column = 2, columnspan = 10)
        
        ttk.Button(text = 'Login', command = self.login_user).grid(row = 3, column = 2)

    def login_user(self):

        ''' Check to see if credentials are correct '''

        if self.username.get() == self.user and self.password.get() == self.password:

            # Destroy the window 

            root.destroy()

        else: 

            '''Prompt user that one or both credentials are incorrect'''

            self.message = Label(text = 'Username or Password incorrect. Try again!', fg = 'Red')
            self.message.grid(row = 6, column = 2)

if __name__ == '__main__':

    root = Tk()
    root.geometry('500x280')
    application = kq(root)

    root.mainloop()
