import tkinter as Tk
import tkinter.ttk as ttk

class listingEvenement:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("Inventaire")
        self.windows.geometry("1024x720")
        self.windows.resizable(False, False)
        self.windows.configure(bg='black')

        self.frame0 = Tk.Frame(self.windows, bg='black')
        self.frame0.grid(column=0 , row=0, padx=10, pady=20)
        
        self.frame1 = Tk.Frame(self.windows, bg='black')
        self.frame1.grid(column=0 , row=1, padx=30, pady=20)
        
        self.frame2 = ttk.Frame(self.windows)
        self.frame2.grid(column=0 , row=2, padx=10)
        
        self.frame3 = Tk.Frame(self.windows, bg='black')
        self.frame3.grid(column=0 , row=3, padx=10)
        
        
        self.label1 = Tk.Label(self.frame0, text="INVENTAIRE DES EVENEMENTS", font=("helvetica", 32), bg='black', fg='red')
        self.label1.grid(column=0 , row=0, padx=10, pady=10)
        
        self.champ1 = ttk.Entry(self.frame1, width=25, font=("helvetica", 14))
        self.champ1.grid(column=0 , row=0)
        
        self.rechercher = ttk.Button(self.frame1, text="Rechercher", width=10)
        self.rechercher.grid(column=1 , row=0)
        
        cols = ("first", "second", "third", "last","five","select")
        self.data_grid = ttk.Treeview(self.frame2, show="headings",columns=cols, height=20)
        
        for col in cols:
            self.data_grid.column(col, width=190)
            self.data_grid.heading(col, text=col)
            
        self.data_grid.column("select", width=50)
        self.data_grid.heading("select", text="select")
        self.data_grid.grid(column=0 , row=0)
        
        self.button1 = ttk.Button(self.frame3, text="Ajouter")
        self.button1.grid(row=3, column=0, padx=10, pady=30)
        self.button2 = ttk.Button(self.frame3, text="Supprimer")
        self.button2.grid(row=3, column=1,padx=10, pady=30)
        self.button3 = ttk.Button(self.frame3, text="Modifier")
        self.button3.grid(row=3, column=2,padx=10, pady=30)
        
        
        
fenetre = Tk.Tk()
fenetre1 = listingEvenement(fenetre)
fenetre.mainloop()
         