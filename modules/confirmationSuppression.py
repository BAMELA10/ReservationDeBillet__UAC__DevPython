#boite de confirmation de suppression
import tkinter as Tk

class mainProgramme:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("")
        self.windows.geometry("400x200")
        self.windows.resizable(False, False)
        self.windows.configure(bg ='black')
        
        self.frame1 = Tk.Frame(self.windows, bd=5, width = self.windows.winfo_vrootwidth(), height = self.windows.winfo_vrootheight())     
        self.frame1.configure(bg ='black')
        self.frame1.pack(expand=True)
        
        self.frame2 = Tk.Frame(self.windows, bd=5, width = self.windows.winfo_vrootwidth(), height = self.windows.winfo_vrootheight())     
        self.frame2.configure(bg ='black')
        self.frame2.pack(side='bottom')
        
        self.label1 = Tk.Label(self.frame1, text="Are you sure do you want to continue this operation?", bg='black')
        self.label1.configure(font = ("helvetica"), fg = 'red')
        self.label1.pack(expand=True)
        
        self.OkButton = Tk.Button(self.frame2, text = 'OK', bg = "red", width = 15)
        self.OkButton.grid(row=1 , column=2, padx=30, pady= 40)
        
        self.SuppButton = Tk.Button(self.frame2, text = 'Annuler', bg = "red", width = 15)
        self.SuppButton.grid(row=1 , column=3, padx=30, pady= 40)
        
fenetre = Tk.Tk()
fenetre1 = mainProgramme(fenetre)
fenetre.mainloop()
         