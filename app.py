# from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import os


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Title
        self.title("Re-Protest")

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_height = 200
        window_width = 300

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        # self.resizable(False, False)
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        self.iconphoto(False, tk.PhotoImage(file='./assets/favicon.png'))

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="True")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Globals
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.client_id = tk.StringVar()
        self.client_secret = tk.StringVar()

        self.frames = {}
        self.MainMenu = MainMenu
        self.ConfigPage = ConfigPage
        self.DeleteMenu = DeleteMenu
        self.RestoreMenu = RestoreMenu
        self.SaveMenu = SaveMenu

        for F in {MainMenu, ConfigPage, DeleteMenu, RestoreMenu, SaveMenu}:
            frame = F(self,container)
            self.frames[F]= frame
            frame.grid(row=0, column=0, sticky="news")
        
        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class MainMenu(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        self.grid(sticky="news")

        label = tk.Label(self, text="Re-Protest")
        label.grid(pady=0, padx=0)

        ttk.Button(
            self, 
            text='Configure', 
            cursor="hand2", 
            command=lambda:parent.show_frame(parent.ConfigPage)
        ).grid(
            column=0,
            row=0,
            pady=7
        )

        ttk.Button(
            self, 
            text='Save Comments', 
            cursor="hand2", 
            command=lambda:parent.show_frame(parent.SaveMenu)
        ).grid(
            column=0,
            row=1,
            pady=7
        )

        ttk.Button(
            self, 
            text='Delete Comments', 
            cursor="hand2", 
            command=lambda:parent.show_frame(parent.DeleteMenu)
        ).grid(
            column=0,
            row=2,
            pady=7
        )

        ttk.Button(
            self, 
            text='Restore Comments', 
            cursor="hand2", 
            command=lambda:parent.show_frame(parent.RestoreMenu)
        ).grid(
            column=0,
            row=3,
            pady=7
        )

        print(username)
        
class ConfigPage(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        
class DeleteMenu(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Re-Protest")
        label.grid(pady=0, padx=0)

class RestoreMenu(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Re-Protest")
        label.grid(pady=0, padx=0)

class SaveMenu(tk.Frame):
    def __init__(self, parent, container):
        super().__init__(container)

        label = tk.Label(self, text="Re-Protest")
        label.grid(pady=0, padx=0)

# def selectDir(pathVar: str, entryField:ttk.Entry) -> str:
#     pathVar = fd.askdirectory(parent=root,initialdir="./",title='Save to directory...')
#     entryField.delete(0, tk.END)
#     entryField.insert(0,pathVar)


# def dataFrame(root: tk.Tk):

#     headerFrame(root)

#     frame = ttk.Frame(root)
#     frame.pack()

#     directory_entry = ttk.Entry(frame,textvariable=dirname)
#     directory_entry.insert(0,dirname)
#     directory_entry.grid(column=0, row=0, padx=5, pady=7)

#     ttk.Button(
#         frame,
#         text="Select Directory",
#         cursor="hand2",
#         command=lambda:selectDir(dirname, directory_entry)
#     ).grid(
#         column=1,
#         row=0,
#         pady=7
#     )`


username=''
password=''
client_id=''
client_secret=''
dirname='./'

if __name__ == "__main__":
    app = App()
    app.mainloop()


