#fenetre de connexion du user
#fenetre de creation du user
import tkinter as tk
from tkinter import ttk, messagebox
import tkcalendar as tkc
from models import *
import datetime as dt

class ReservationCreation:
    def __init__(self, windows1):
        windows1 = windows1
        windows1.title("ReservationCreation")
        windows1.geometry("800x600")
        windows1.resizable(False, False)
        #windows1

        #isertion des elements de la fenetre
        frame1 = tk.Frame(windows1, relief=tk.SUNKEN,  width=200, height=600)
        frame1.configure( bg="red")
        frame1.grid(column=1, row=0)
        
        frame2 = tk.Frame(windows1, relief=tk.SUNKEN, width=600, height=600)
        frame2.configure( bg="black")
        frame2.grid(column=2, row=0)
        
        frame3 = tk.Frame(frame2, relief=tk.SUNKEN, width=10, height=10)
        frame3.configure( bg="black")
        frame3.grid(column=1, row=0, padx=52)
        
        frame4 = tk.Frame(frame2, relief=tk.SUNKEN, width=150, height=200)
        frame4.configure( bg="black")
        frame4.grid(column=1, row=1, padx=52)
        
        title = tk.Label(frame3, text="Creation d'une reservation")
        title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        title.grid(column=0, row=0, pady=40)
        
        labelx = tk.Label(frame4, text="Code de la reservation")
        labelx.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        labelx.grid(column=0, row=0)
        
        champ_ex = tk.Entry(frame4, width=15, font=("helvetica", 18),state="disable", bg="#D3D3D3")
        champ_ex.grid(column=1, row=0, pady=30)

        label1 = tk.Label(frame4, text="Statut de la reservation")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=2)
        
        champ_e1 = ttk.Combobox(frame4, value=["Pris en compte"])
        champ_e1.insert(0, "Pris en compte")
        champ_e1.config(state="disabled",exportselection=0)
        champ_e1.grid(column=1, row=2, pady=30)
        
        label2 = tk.Label(frame4, text="Date de la reservation", bg="black")
        label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        label2.grid(column=0, row=1)
        
        champ_e2 = tkc.DateEntry(frame4, width=10, font=("helvetica", 18))
        champ_e2.delete(0, tk.END)
        champ_e2.insert(0, dt.date.today())
        champ_e2.config(state="disabled")
        champ_e2.grid(column=1, row=1, pady=30)
        
        label3 = tk.Label(frame4, text="Evenement", bg="black")
        label3.configure(font=("helvetica", 14), width=25,fg= "red" )
        label3.grid(column=0, row=3)

        value0 = event_all()
        champ_e3 = ttk.Combobox(frame4, value=value0)
        champ_e3.grid(column=1, row=3, pady=30)

        label4 = tk.Label(frame4, text="Utilisateur", bg="black")
        label4.configure(font=("helvetica", 14), width=25,fg= "red" )
        label4.grid(column=0, row=4)
        
        values1 = users_all()
        champ_e4 = ttk.Combobox(frame4, value=values1)
        champ_e4.grid(column=1, row=4, pady=30)
        
        btn_validate = tk.Button(frame4, text="OK",width=15,bg="red", command=users_all)
        btn_validate.grid(column=0, row=5, pady=20)

        btn_back = tk.Button(frame4, text="Annuler",width=15, bg="red",command=windows1.destroy)
        btn_back.grid(column=1, row=5, pady=20)

    
        
        def get_value_of_entry(self):
            value = [
                str(champ_e1.get()),
                str(champ_e2.get_date()),
                (champ_e3.get()),
                (champ_e4.get())
            ]
            return value
        
windows1 = tk.Tk()
windows11 = ReservationCreation(windows1)
windows1.mainloop()
