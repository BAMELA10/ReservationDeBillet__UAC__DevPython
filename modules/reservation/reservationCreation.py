#fenetre de connexion du user
#fenetre de creation du user
import tkinter as tk
from tkinter import ttk, messagebox
import tkcalendar as tkc
from models import *
import datetime as dt
def event_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select id, intitulé from event")
        return cursor.fetchall()
def users_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select id, username from users")
        return cursor.fetchall()
class ReservationCreation:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("ReservationCreation")
        self.windows.geometry("800x600")
        self.windows.resizable(False, False)
        #self.windows

        #isertion des elements de la fenetre
        self.frame1 = tk.Frame(self.windows, relief=tk.SUNKEN,  width=200, height=600)
        self.frame1.configure( bg="red")
        self.frame1.grid(column=1, row=0)
        
        self.frame2 = tk.Frame(self.windows, relief=tk.SUNKEN, width=600, height=600)
        self.frame2.configure( bg="black")
        self.frame2.grid(column=2, row=0)
        
        self.frame3 = tk.Frame(self.frame2, relief=tk.SUNKEN, width=10, height=10)
        self.frame3.configure( bg="black")
        self.frame3.grid(column=1, row=0, padx=52)
        
        self.frame4 = tk.Frame(self.frame2, relief=tk.SUNKEN, width=150, height=200)
        self.frame4.configure( bg="black")
        self.frame4.grid(column=1, row=1, padx=52)
        
        self.title = tk.Label(self.frame3, text="Creation d'une reservation")
        self.title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        self.title.grid(column=0, row=0, pady=40)
        
        self.labelx = tk.Label(self.frame4, text="Code de la reservation")
        self.labelx.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        self.labelx.grid(column=0, row=0)
        
        self.champ_ex = tk.Entry(self.frame4, width=15, font=("helvetica", 18),state="disable", bg="#D3D3D3")
        self.champ_ex.grid(column=1, row=0, pady=30)

        self.label1 = tk.Label(self.frame4, text="Statut de la reservation")
        self.label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        self.label1.grid(column=0, row=2)
        
        self.champ_e1 = ttk.Combobox(self.frame4, value=["Pris en compte"])
        self.champ_e1.insert(0, "Pris en compte")
        self.champ_e1.config(state="disabled",exportselection=0)
        self.champ_e1.grid(column=1, row=2, pady=30)
        
        self.label2 = tk.Label(self.frame4, text="Date de la reservation", bg="black")
        self.label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        self.label2.grid(column=0, row=1)
        
        self.champ_e2 = tkc.DateEntry(self.frame4, width=10, font=("helvetica", 18))
        self.champ_e2.delete(0, tk.END)
        self.champ_e2.insert(0, dt.date.today())
        self.champ_e2.config(state="disabled")
        self.champ_e2.grid(column=1, row=1, pady=30)
        
        self.label3 = tk.Label(self.frame4, text="Evenement", bg="black")
        self.label3.configure(font=("helvetica", 14), width=25,fg= "red" )
        self.label3.grid(column=0, row=3)

        value0 = event_all()
        self.champ_e3 = ttk.Combobox(self.frame4, value=value0)
        self.champ_e3.grid(column=1, row=3, pady=30)

        self.label4 = tk.Label(self.frame4, text="Utilisateur", bg="black")
        self.label4.configure(font=("helvetica", 14), width=25,fg= "red" )
        self.label4.grid(column=0, row=4)
        
        values1 = users_all()
        self.champ_e4 = ttk.Combobox(self.frame4, value=values1)
        self.champ_e4.grid(column=1, row=4, pady=30)
        
        self.btn_validate = tk.Button(self.frame4, text="OK",width=15,bg="red", command=users_all)
        self.btn_validate.grid(column=0, row=5, pady=20)

        self.btn_back = tk.Button(self.frame4, text="Annuler",width=15, bg="red",command=self.windows.destroy)
        self.btn_back.grid(column=1, row=5, pady=20)

    
        
        def get_value_of_entry(self):
            value = [
                str(self.champ_e1.get()),
                str(self.champ_e2.get_date()),
                (self.champ_e3.get()),
                (self.champ_e4.get())
            ]
            return value
        
windows = tk.Tk()
windows1 = ReservationCreation(windows)
windows.mainloop()
