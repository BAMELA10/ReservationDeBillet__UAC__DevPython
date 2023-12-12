import tkinter as Tk
import tkinter.ttk as ttk
import models
from connect import connector
def reservation_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select code, date_reservation, status_reservation,id_event,id_users from reservation")
        return cursor.fetchall()
class listingReservation:
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
        
        
        self.label1 = Tk.Label(self.frame0, text="Listing des Reservations", font=("helvetica", 32), bg='black', fg='red')
        self.label1.grid(column=0 , row=0, padx=10, pady=10)
        
        self.champ1 = ttk.Entry(self.frame1, width=25, font=("helvetica", 14))
        self.champ1.grid(column=0 , row=0)
        
        self.rechercher = ttk.Button(self.frame1, text="Rechercher", width=10)
        self.rechercher.grid(column=1 , row=0)
        
        cols = ("Code", "Date reservation", "Statut", "Evenement","Utilisateur",)
        self.data_grid = ttk.Treeview(self.frame2, show="headings",columns=cols, height=20)
        
        for col in cols:
            self.data_grid.column(col, width=200, anchor="center")
            self.data_grid.heading(col, text=col)
            
        rows = reservation_all()
        for row in rows:
            self.data_grid.insert("","end",value=row)
        self.data_grid.grid(column=0 , row=0)
        
        self.button1 = ttk.Button(self.frame3, text="Ajouter")
        self.button1.grid(row=3, column=0, padx=10, pady=30)
        self.button2 = ttk.Button(self.frame3, text="Annuler")
        self.button2.grid(row=3, column=1,padx=10, pady=30)
        self.button3 = ttk.Button(self.frame3, text="Modifier")
        self.button3.grid(row=3, column=2,padx=10, pady=30)
        
        
        
fenetre = Tk.Tk()
fenetre1 = listingReservation(fenetre)
fenetre.mainloop()
         