# from tkinter import *
# from tkinter.ttk import *
import tkinter as tk
from tkinter import ttk


def windowSetup() -> tk.Tk:
    # Setup window
    w = tk.Tk()

    # Title
    w.title("Re-Protest")

    # Size and position
    screen_width = w.winfo_screenwidth()
    screen_height = w.winfo_screenheight()
    window_height = 300
    window_width = 450

    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    w.resizable(False, False)
    w.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    # Icon
    w.iconphoto(False, tk.PhotoImage(file='./assets/favicon.png'))

    return(w)

def clearFrame(frame: tk.Frame):
    for widget in frame.winfo_children():
        widget.destroy()
    
def clearWindow(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()

def switchFrames(window, currentFrame: tk.Frame, nextFrame):
    clearFrame(currentFrame)
    clearWindow(window)
    nextFrame(window)

def headerFrame(root: tk.Tk):
    frame=ttk.Frame(root)
    frame.pack()
    top_text_label = ttk.Label(frame, text="blablablabla\nasdlkjaslgjlfgsdkj\nofusdlgksjdfglsfdgjsfdlkj").grid(column=0, row=0, padx=15, pady=15, sticky="ns")
    frame.grid_rowconfigure(0, weight=2)

def userDetails(root: tk.Tk):

    headerFrame(root)

    frame = ttk.Frame(root)
    # frame.pack(padx=10,pady=10,fill='x',expand=True)
    # frame.pack(fill='x')
    frame.pack()

    # Username
    username_label = ttk.Label(frame,text='Username').grid(column=0, row=1, sticky="w", padx=5, pady=5)   
    username_entry = ttk.Entry(frame,textvariable=username).grid(column=1, row=1, sticky="w", padx=5, pady=5)
    frame.grid_rowconfigure(1, weight=1)

    # Password
    password_label = ttk.Label(frame,text='Password').grid(column=0, row=2, sticky="w", padx=5, pady=5)
    password_entry = ttk.Entry(frame,textvariable=password,show="*").grid(column=1, row=2, sticky="w", padx=5, pady=5)
    frame.grid_rowconfigure(2, weight=1)

    # Client ID
    client_label = ttk.Label(frame,text='Client ID').grid(column=0, row=3, sticky="w", padx=5, pady=5)
    client_entry = ttk.Entry(frame,textvariable=client_id).grid(column=1, row=3, sticky="w", padx=5, pady=5)
    frame.grid_rowconfigure(3, weight=1)

    # Client Secret
    secret_label = ttk.Label(frame,text='Client Secret').grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
    secret_entry = ttk.Entry(frame,textvariable=client_secret,show="*").grid(column=1, row=4, sticky="w", padx=5, pady=5)
    frame.grid_rowconfigure(4, weight=1)

    ttk.Button(
        frame, 
        text='Continue', 
        cursor="hand2", 
        command=lambda:switchFrames(root, frame, dataFrame)
    ).grid(
        column=0,
        row=5,
        sticky="se",
        columnspan=2
    )
    frame.grid_rowconfigure(5,weight=2)

def dataFrame(root: tk.Tk):

    frame = ttk.Frame(root)
    frame.pack()



    ttk.Button(
        frame, 
        text='Back', 
        cursor="hand2", 
        command=lambda:switchFrames(root, frame, userDetails)
    ).grid(
        column=0,
        row=0,
        sticky="se"
    )
    ttk.Button(
        frame, 
        text='Continue', 
        cursor="hand2", 
        command=lambda:switchFrames(root, frame, userDetails)
    ).grid(
        column=1,
        row=0,
        sticky="se"
    )
root = windowSetup()

username = tk.StringVar()
password = tk.StringVar()
client_id = tk.StringVar()
client_secret = tk.StringVar()

userDetails(root)

root.mainloop()
