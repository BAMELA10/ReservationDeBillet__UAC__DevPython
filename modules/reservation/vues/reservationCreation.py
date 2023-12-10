#fenetre de connexion du user
#fenetre de creation du user
import tkinter as tk
import center as ct
import ttk
class ReservationCreation:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("ReservationCreation")
        self.windows.geometry("800x600")
        self.windows.resizable(False, False)
        #self.windows

        #isertion des elements de la fenetre
        self.frame1 = tk.Frame(self.windows, bd=0, relief=tk.SUNKEN,  width=300, height=400)
        self.frame1.configure( bg="red")
        self.frame1.pack(side='left')
        self.frame2 = tk.Frame(self.windows, bd=0, relief=tk.SUNKEN,  width=500, height=400)
        self.frame2.configure( bg="black")
        self.frame2.pack(side='right')




windows = tk.Tk()
windows1 = ReservationCreation(windows)
ct.center(windows)
windows.mainloop()