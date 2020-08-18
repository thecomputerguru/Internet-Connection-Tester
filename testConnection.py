#Python Network Connection Tester
#
#
#Import required modules
import socket as s
import tkinter as tk
from tkinter import messagebox

def connect():
    root = tk.Tk() #Initialize Tkinter to withdraw top window when messagebox shows
    try: #Try to connect to Google.com
        connection = s.create_connection((s.gethostbyname('google.com'),80),2) #Connect to Google.com
        connection.close() #Close connection to Google.com
        root.withdraw() #Hide top tk empty window when showing messagebox
        messagebox.showinfo('Network Info','Your computer is connected to the internet') #Show that computer is connected to the internet
    except:
        root.withdraw()
        messagebox.showerror('Network Error','Your computer is not connected to the internet')
connect()
