#boite de confirmation de success d'une operation
import tkinter as Tk
''' import center as ct '''
class Confirmation:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("Confirmation")
        self.windows.geometry("400x200")
        self.windows.resizable(False, False)
        self.windows.configure(bg='black')
        self.windows.iconbitmap("")
        
        self.frame1 = Tk.Frame(self.windows, bd=5, width = self.windows.winfo_vrootwidth(), height = self.windows.winfo_vrootheight())     
        self.frame1.configure(bg ='black')
        self.frame1.pack(expand=True)
        
        self.frame2 = Tk.Frame(self.windows, bd=5, width = self.windows.winfo_vrootwidth(), height = self.windows.winfo_vrootheight())     
        self.frame2.configure(bg ='black')
        self.frame2.pack(side='bottom')
        
        self.label1 = Tk.Label(self.frame1, text=" The Operation was completed succesfully", bg='black')
        self.label1.configure(font = ("helvetica"), fg = 'red')
        self.label1.pack(expand=True)
        
        self.OkButton = Tk.Button(self.frame2, text = 'OK', bg = "red", width = 15)
        self.OkButton.grid(row=1 , column=2, padx=30, pady= 40)
        
        
        
        
        
        
fenetre = Tk.Tk()
fenetre1 = Confirmation(fenetre)
''' ct.center(fenetre) '''
fenetre.mainloop()
         