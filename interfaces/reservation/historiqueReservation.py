#fenetre d'historique de reservation
import tkinter as Tk

class mainProgramme:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title(" Home ")
        self.windows.geometry("1024x720")
        self.windows.resizable(False, False)
        
fenetre = Tk.Tk()
fenetre1 = mainProgramme(fenetre)
fenetre.mainloop()
         