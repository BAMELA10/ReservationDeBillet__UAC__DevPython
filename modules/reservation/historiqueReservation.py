from connect import connector
import tkinter as tk
from tkinter import ttk, messagebox
import tkcalendar as tkc
from models import *
import datetime as dt

def reservation_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select code, date_reservation, number_place, status_reservation,id_event,id_users from reservation")
        return cursor.fetchall()
def reservation_all_for_print():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select reservation.code, date_reservation, reservation.number_place, status_reservation, users.username, event.intitulé from reservation inner join users on reservation.id_users = users.id inner join event on reservation.id_event = event.id")
        return cursor.fetchall()
    
def event_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select intitulé from event")
        return cursor.fetchall()
    
def users_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select username from users")
        return cursor.fetchall()

def get_user_by_name(name):
    connector.ping()
    cursor = connector.cursor()
    cursor.execute("select id from users where username = %s", (name,))
    return cursor.fetchall()

def get_event_by_name(name):
    connector.ping()
    cursor = connector.cursor()
    cursor.execute("select id from event where intitulé = %s", (name,))
    return cursor.fetchall()
    
class listingReservation:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("Inventaire")
        self.windows.geometry("1024x720")
        self.windows.resizable(False, False)
        self.windows.configure(bg='black')

        self.frame0 = tk.Frame(self.windows, bg='black')
        self.frame0.grid(column=0 , row=0, padx=10, pady=20)
        
        self.frame1 = tk.Frame(self.windows, bg='black')
        self.frame1.grid(column=0 , row=1, padx=30, pady=20)
        
        self.frame2 = ttk.Frame(self.windows)
        self.frame2.grid(column=0 , row=2, padx=10)
        
        self.frame3 = tk.Frame(self.windows, bg='black')
        self.frame3.grid(column=0 , row=3, padx=10)
        
        
        self.label1 = tk.Label(self.frame0, text="Listing des Reservations", font=("helvetica", 32), bg='black', fg='red')
        self.label1.grid(column=0 , row=0, padx=10, pady=10)
        
        self.champ1 = ttk.Entry(self.frame1, width=25, font=("helvetica", 14))
        self.champ1.grid(column=0 , row=0)
        
        self.rechercher = ttk.Button(self.frame1, text="Rechercher", width=10)
        self.rechercher.grid(column=1 , row=0)
        
        cols = ("Code", "Date reservation","Nbre Place", "Statut","Utilisateur","Evenement")
        self.data_grid = ttk.Treeview(self.frame2, show="headings",columns=cols, height=20)
        
        for col in cols:
            self.data_grid.column(col, width=167, anchor="center")
            self.data_grid.heading(col, text=col)
            
        rows = reservation_all_for_print()
        for row in rows:
            self.data_grid.insert("","end",value=row)
        self.data_grid.grid(column=0 , row=0)
        
        self.button1 = ttk.Button(self.frame3, text="Ajouter", command=self.open_add_reservation)
        self.button1.grid(row=3, column=0, padx=10, pady=30)
        self.button2 = ttk.Button(self.frame3, text="Rafraihir", command=self.refresh)
        self.button2.grid(row=3, column=1,padx=10, pady=30)
        self.button3 = ttk.Button(self.frame3, text="Modifier",command=self.open_edit_reservation)
        self.button3.grid(row=3, column=2,padx=10, pady=30)
        self.button3 = ttk.Button(self.frame3, text="Annulation",command=self.cancel_reservation)
        self.button3.grid(row=3, column=3,padx=10, pady=30)
        
    def select_item(self):
        reservation = self.data_grid.selection()
        if reservation:
            reservation_value = self.data_grid.item(reservation,"values")
        return reservation_value
    
    def open_add_reservation(self):
        global windows1
        windows1 = tk.Toplevel(self.windows)
        windows1 = windows1
        windows1.title("ReservationCreation")
        windows1.geometry("823x600")
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
        
        global champ_ex
        champ_ex = tk.Entry(frame4, width=15, font=("helvetica", 18),state="disable", bg="#D3D3D3")
        champ_ex.grid(column=1, row=0, pady=23)

        label1 = tk.Label(frame4, text="Statut de la reservation")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=2)
        
        global champ_e1
        champ_e1 = ttk.Combobox(frame4, value=["Considéré"])
        champ_e1.insert(0, "Considéré")
        champ_e1.config(state="disabled",exportselection=0)
        champ_e1.grid(column=1, row=2, pady=23)
        
        label2 = tk.Label(frame4, text="Date de la reservation", bg="black")
        label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        label2.grid(column=0, row=1)
        
        global champ_e2
        champ_e2 = tkc.DateEntry(frame4, width=10, font=("helvetica", 18))
        champ_e2.delete(0, tk.END)
        champ_e2.insert(0, dt.date.today().strftime("%d-%m-%y"))
        champ_e2.config(state="disabled")
        champ_e2.grid(column=1, row=1, pady=23)
        
        label3 = tk.Label(frame4, text="Evenement", bg="black")
        label3.configure(font=("helvetica", 14), width=25,fg= "red" )
        label3.grid(column=0, row=3)
        
        global champ_e3
        value0 = event_all()
        champ_e3 = ttk.Combobox(frame4, value=value0)
        champ_e3.grid(column=1, row=3, pady=23)

        label4 = tk.Label(frame4, text="Utilisateur", bg="black")
        label4.configure(font=("helvetica", 14), width=25,fg= "red" )
        label4.grid(column=0, row=4)
        
        global champ_e4
        values1 = users_all()
        champ_e4 = ttk.Combobox(frame4, value=values1)
        champ_e4.grid(column=1, row=4, pady=23)
        
        label5 = tk.Label(frame4, text="Nombres Places", bg="black")
        label5.configure(font=("helvetica", 14), width=25,fg= "red" )
        label5.grid(column=0, row=5)
        
        global champ_e5
        champ_e5 = ttk.Entry(frame4)
        champ_e5.grid(column=1, row=5, pady=23)
        
        btn_validate = tk.Button(frame4, text="OK",width=15,bg="red",command=self.add_reservation)
        btn_validate.grid(column=0, row=6, pady=23)

        btn_back = tk.Button(frame4, text="Annuler",width=15, bg="red",command=windows1.destroy)
        btn_back.grid(column=1, row=6, pady=23)
        
    def refresh(self):
        connector.ping()
        self.windows.destroy()
        rows = reservation_all()
        fenetre = tk.Tk()
        fenetre1 = listingReservation(fenetre)
        fenetre.mainloop()
        
    def get_value_of_entry(self):
            value = [
                str(champ_e1.get()),
                str(champ_e2.get_date()),
                (champ_e3.get()),
                (champ_e4.get()),
                int(champ_e5.get())
            ]
            return value
           
    def add_reservation(self):
        value = self.get_value_of_entry()
        list_tuple_id_user = get_user_by_name(value[3].strip("{}"))
        list_tuple_id_event =  get_event_by_name(value[2].strip("{}"))
        tuple_id_user = list_tuple_id_user[0]
        tuple_id_event = list_tuple_id_event[0]
        id_user = tuple_id_user[0]
        id_event = tuple_id_event[0]
        reservation1 = reservation(id_user, id_event, value[0], value[4], "",value[1])
        result = reservation1.create_reservation()
        if result == True:
            messagebox.showinfo("succes","success")
        else :
            messagebox.showinfo("lose","lose")
        windows1.destroy()
        self.refresh()
        
    
    def cancel_reservation(self):
        result = False
        current_value = self.select_item()
        code_current_value = current_value[0]
        list_tuple_id_user = get_user_by_name(current_value[4])
        list_tuple_id_event =  get_event_by_name(current_value[5])
        tuple_id_user = list_tuple_id_user[0]
        tuple_id_event = list_tuple_id_event[0]
        id_user = tuple_id_user[0]
        id_event = tuple_id_event[0]
        reservation1 = reservation(id_user, id_event, current_value[3],current_value[2],current_value[0],current_value[1])
        result = reservation1.cancel_reservation(current_value[0])
        if result != True:
            messagebox.showinfo("lose","lose")
        else:
            messagebox.showinfo("succes","success")
        self.refresh()
        
    def open_edit_reservation(self):
        pevious_data = self.select_item()
        
        global windows2
        windows2 = tk.Toplevel(self.windows)
        windows2 = windows2
        windows2.title("ReservationEdit")
        windows2.geometry("823x600")
        windows2.resizable(False, False)
        #windows1

        #isertion des elements de la fenetre
        frame1 = tk.Frame(windows2, relief=tk.SUNKEN,  width=200, height=600)
        frame1.configure( bg="red")
        frame1.grid(column=1, row=0)
        
        frame2 = tk.Frame(windows2, relief=tk.SUNKEN, width=600, height=600)
        frame2.configure( bg="black")
        frame2.grid(column=2, row=0)
        
        frame3 = tk.Frame(frame2, relief=tk.SUNKEN, width=10, height=10)
        frame3.configure( bg="black")
        frame3.grid(column=1, row=0, padx=52)
        
        frame4 = tk.Frame(frame2, relief=tk.SUNKEN, width=150, height=200)
        frame4.configure( bg="black")
        frame4.grid(column=1, row=1, padx=52)
        
        title = tk.Label(frame3, text="Modification d'une reservation")
        title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        title.grid(column=0, row=0, pady=40)
        
        labelx = tk.Label(frame4, text="Code de la reservation")
        labelx.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        labelx.grid(column=0, row=0)
        
        global champ_mx
        champ_mx = tk.Entry(frame4, width=15, font=("helvetica", 18),state="disable", bg="#D3D3D3")
        champ_mx.grid(column=1, row=0, pady=23)

        label1 = tk.Label(frame4, text="Statut de la reservation")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=2)
        
        global champ_m1
        champ_m1 = ttk.Combobox(frame4, value=["Considéré"])
        champ_m1.insert(0, pevious_data[3])
        champ_m1.config(state="disabled",exportselection=0)
        champ_m1.grid(column=1, row=2, pady=23)
        
        label2 = tk.Label(frame4, text="Date de la reservation", bg="black")
        label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        label2.grid(column=0, row=1)
        
        global champ_m2
        champ_m2 = tkc.DateEntry(frame4, width=10, font=("helvetica", 18))
        champ_m2.delete(0, tk.END)
        date_db = dt.datetime.strptime(pevious_data[1], "%Y-%m-%d")
        date_db = date_db.strftime("%d/%m/%y")
        champ_m2.insert(0, date_db)
        champ_m2.config(state="disabled")
        champ_m2.grid(column=1, row=1, pady=23)
        
        label3 = tk.Label(frame4, text="Evenement", bg="black")
        label3.configure(font=("helvetica", 14), width=25,fg= "red" )
        label3.grid(column=0, row=3)
        
        global champ_m3
        value0 = event_all()
        champ_m3 = ttk.Combobox(frame4, value=value0)
        champ_m3.insert(0, pevious_data[5])
        champ_m3.grid(column=1, row=3, pady=23)

        label4 = tk.Label(frame4, text="Utilisateur", bg="black")
        label4.configure(font=("helvetica", 14), width=25,fg= "red")
        label4.grid(column=0, row=4)
        
        global champ_m4
        values1 = users_all()
        champ_m4 = ttk.Combobox(frame4, value=values1)
        champ_m4.insert(0, pevious_data[4])
        champ_m4.grid(column=1, row=4, pady=23)
        
        label5 = tk.Label(frame4, text="Nombres Places", bg="black")
        label5.configure(font=("helvetica", 14), width=25,fg= "red" )
        label5.grid(column=0, row=5)
        
        global champ_m5
        champ_m5 = ttk.Entry(frame4)
        champ_m5.insert(0, pevious_data[2])
        champ_m5.grid(column=1, row=5, pady=23)
        
        btn_validate = tk.Button(frame4, text="OK",width=15,bg="red",command=self.edit_reservation)
        btn_validate.grid(column=0, row=6, pady=23)

        btn_back = tk.Button(frame4, text="Annuler",width=15, bg="red",command=windows2.destroy)
        btn_back.grid(column=1, row=6, pady=23)
        
    def get_value_of_entry_for_edit(self):
        value = [
            str(champ_m1.get()),
            str(champ_m2.get_date()),
            (champ_m3.get()),
            (champ_m4.get()),
            int(champ_m5.get())
        ]
        return value
    
    def edit_reservation(self):
        current_value = self.select_item()
        value = self.get_value_of_entry_for_edit()
        list_tuple_id_user = get_user_by_name(value[3].strip("{}"))
        list_tuple_id_event =  get_event_by_name(value[2].strip("{}"))
        tuple_id_user = list_tuple_id_user[0]
        tuple_id_event = list_tuple_id_event[0]
        id_user = tuple_id_user[0]
        id_event = tuple_id_event[0]
        reservation1 = reservation(id_user, id_event, value[0], value[4], "",value[1])
        result = reservation1.edit_reservation(current_value[0])
        if result != True:
            messagebox.showinfo("lose","lose")
        else:
            messagebox.showinfo("success","success")
        windows2.destroy()
        self.refresh()
        
        
fenetre = tk.Tk()
fenetre1 = listingReservation(fenetre)
fenetre.mainloop()
         
