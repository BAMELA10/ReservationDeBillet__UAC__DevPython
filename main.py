from modules.main.vues.Home import Home
from modules.main.vues.opening import opening
from modules.users.models import *
from modules.users.listingUser import *
from modules.users.userCreation import *
from modules.reservation.models import *
from modules.reservation.historiqueReservation import *
from modules.evenement.models import *
from modules.evenement.listingEvenement import *

#import interfaces.opening as openg
import tkinter as tk
from tkinter import messagebox
import os
import sys

#fenetre principale du profil d'utilisateur
def login_gui():
    global username
    username = str(champ1.get())
    global password
    password = str(champ2.get())
    user = users(username, password)
    result = user.login_user()
    if result == True:
        messagebox.showinfo("connexion","connected")
        windows.destroy()
        return [True]
    else:
        messagebox.showinfo("connexion", "nom d'utilisateur ou mot de passe incorrect")
        return [False]  

def open_ges_reservation():
    windows = tk.Tk()
    windows1 = listingReservation(windows)
    windows.mainloop()
def deconnexion():
    python = sys.executable
    os.execl(python, os.path.abspath(__file__), *sys.argv)

def get_row_by_id():
    connector.ping()
    curseur = connector.cursor()
    user = get_user_by_name(username)
    user = user[0]
    user = user[0]
    curseur.execute("select reservation.code, date_reservation, reservation.number_place, status_reservation, users.username, event.intitulé from reservation inner join users on reservation.id_users = users.id inner join event on reservation.id_event = event.id where id_users = %s", (user,))
    return curseur.fetchall()

def refresh_mes_reservation(fenetre):
    connector.ping()
    fenetre.destroy()
    rows = get_row_by_id()
    fenetre = tk.Tk()
    fenetre1 = listingReservation(fenetre)
    fenetre1.rows = rows
    cols = ("Code", "Date reservation","Nbre Place", "Statut","Utilisateur","Evenement")
    fenetre1.data_grid = ttk.Treeview(fenetre1.frame2, show="headings",columns=cols, height=20)
    for col in cols:
        fenetre1.data_grid.column(col, width=167, anchor="center")
        fenetre1.data_grid.heading(col, text=col)
    for fenetre1.row in fenetre1.rows:
        fenetre1.data_grid.insert("","end",value=fenetre1.row)
    fenetre1.data_grid.grid(column=0 , row=0)
    fenetre.mainloop()
    
def mes_reservation():
    var = get_row_by_id()
    reservation_w = tk.Tk()
    reservation_w1 = listingReservation(reservation_w)
    reservation_w1.rows = var
    print(reservation_w1.rows)
    cols = ("Code", "Date reservation","Nbre Place", "Statut","Utilisateur","Evenement")
    reservation_w1.data_grid = ttk.Treeview(reservation_w1.frame2, show="headings",columns=cols, height=20)
    for col in cols:
        reservation_w1.data_grid.column(col, width=167, anchor="center")
        reservation_w1.data_grid.heading(col, text=col)
    for reservation_w1.row in reservation_w1.rows:
        reservation_w1.data_grid.insert("","end",value=reservation_w1.row)
    reservation_w1.data_grid.grid(column=0 , row=0)
    reservation_w1.button2 = ttk.Button(reservation_w1.frame3, text="Rafraihir", command=lambda: refresh_mes_reservation(reservation_w))
    reservation_w1.button2.grid(row=3, column=1,padx=10, pady=30)
    reservation_w.mainloop()
    
def mon_profil(fenetre):
    connector.ping()
    curseur = connector.cursor()
    user = get_user_by_name(username)
    user = user[0]
    user = user[0]
    curseur.execute("select username, email, phone, status from users where id = %s", (user,))
    var = curseur.fetchone()
    fenetre = tk.Toplevel(fenetre)
    fenetre.title("Inventaire")
    fenetre.geometry("800x700")
    fenetre.resizable(False, False)
    fenetre.configure(bg='black')

    
    frame1 = tk.Frame(fenetre, bg='black')
    frame1.grid(column=0 , row=1, padx=30, pady=20)
    
    
    label1 = tk.Label(frame1, text="Profil de l'utilisateur")
    label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label1.grid(column=0, row=1,pady=50)
    
    label2 = tk.Label(frame1, text="Nom de l'utilisateur :")
    label2.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label2.grid(column=0, row=2,pady=50)
    
    label3 = tk.Label(frame1, text="Email de l'utilisateur :")
    label3.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label3.grid(column=0, row=3,pady=50)
    
    label4 = tk.Label(frame1, text="Telephone de l'utilisateur :")
    label4.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label4.grid(column=0, row=4,pady=50)
    
    label5 = tk.Label(frame1, text="Privilège de l'utilisateur :")
    label5.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label5.grid(column=0, row=5,pady=50)
    
    
    label7 = tk.Label(frame1, text=var[0])
    label7.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label7.grid(column=1, row=2,pady=50)
    
    label8 = tk.Label(frame1, text=var[1])
    label8.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label8.grid(column=1, row=3,pady=50)
    
    label9 = tk.Label(frame1, text=str(var[2]))
    label9.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label9.grid(column=1, row=4,pady=50)
    
    label0 = tk.Label(frame1, text=var[3])
    label0.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label0.grid(column=1, row=5,pady=50)

def open_ges_event():
    windows = tk.Tk()
    windows1 = listingEvenement(windows)
    windows.mainloop()
    
def open_ges_users():
    windows = tk.Tk()
    windows1 = listingUser(windows)
    windows.mainloop()
    
def open_create_user(fenetre):
    fenetre.destroy()
    windows = tk.Tk()
    windows1 = UserCreation(windows)
    windows.mainloop()
    deconnexion()

    
            
if __name__ == '__main__':
    openingx = tk.Tk()
    opening1 = opening(openingx)
    opening1.center()
    openingx.after(5000, openingx.destroy)
    openingx.mainloop()
    windows = tk.Tk()
    windows.title("EventCreation")
    windows.geometry("800x400")
    windows.resizable(False, False)
    windows.configure(bg="black")
    #windows

    #isertion des elements de la fenetre
    frame1 = tk.Frame(windows, relief=tk.SUNKEN,  width=150, height=400)
    frame1.configure( bg="red")
    frame1.grid(column=1, row=0)
    
    frame2 = tk.Frame(windows, relief=tk.SUNKEN, width=250, height=400)
    frame2.configure( bg="black")
    frame2.grid(column=2, row=0)
    
    frame3 = tk.Frame(frame2, relief=tk.SUNKEN, width=10, height=10)
    frame3.configure( bg="black")
    frame3.grid(column=1, row=0)
    
    frame4 = tk.Frame(frame2, relief=tk.SUNKEN, width=150, height=200)
    frame4.configure( bg="black")
    frame4.grid(column=1, row=1)
    
    #Insertion du titre de la fenetre 
    title = tk.Label(frame3, text="Connexion")
    title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
    title.grid(column=0, row=0, pady=30)
    
    label1 = tk.Label(frame4, text="Nom de l'utilisateur")
    label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
    label1.grid(column=0, row=1)
    
    champ1 = tk.Entry(frame4, width=20, font=("helvetica", 18),)
    champ1.grid(column=1, row=1, pady=30)
    
    
    label2 = tk.Label(frame4, text="Mot de passe", bg="black")
    label2.configure(font=("helvetica", 14), width=25,fg= "red" )
    label2.grid(column=0, row=2)
    
    champ2 = tk.Entry(frame4, width=20, font=("helvetica", 18))
    champ2.grid(column=1, row=2, pady=30)

    
    btn_validate = tk.Button(frame4, text="OK",width=15,bg="red", command=login_gui)
    btn_validate.grid(column=0, row=5, pady=30)

    btn_back = tk.Button(frame4, text="Annuler",width=15, bg="red", command=windows.destroy)
    btn_back.grid(column=1, row=5, pady=30)
    
    btn_sign_up = tk.Button(frame4, text="S'inscrire",width=15, bg="red", command=lambda: open_create_user(windows))
    btn_sign_up.grid(column=0, row=6, pady=5)
    windows.mainloop()
    
    user = users(username, password)
    result = user.login_user()
    if result == True:
        connector.ping()
        curseur = connector.cursor()
        curseur.execute("select status from users where username = %s",(username,))
        result = curseur.fetchone()
        result = result[0]
        print(username)
        if result == 'Standard':
            
            home = tk.Tk()
            app = Home(home, username)
            app.button1 = tk.Button(app.frame1Frame2, bd=2, text ="Gestion. Utilisateur", bg='red', fg='black',width=30, height=1, state=tk.DISABLED)
            app.button1.configure(font=('helvetica', 12))
            app.button1.grid(row=3, column=1, padx=150, pady=20, ipadx=0, ipady=5)
            app.button3 = tk.Button(app.frame1Frame2, bd=2, text ="Gestion. Evenement", bg='red', fg='black',width=30, height=1,state=tk.DISABLED)
            app.button3.configure(font=('helvetica', 12)) 
            app.button3.grid(row=5, column=1, padx=150, pady=20, ipadx=0, ipady=5)
            app.button2 = tk.Button(app.frame1Frame2, bd=2, text ="Gestion. Reservation", bg='red', fg='black',width=30, height=1, command=open_ges_reservation, state=tk.DISABLED)
            app.button2.configure(font=('helvetica', 12))
            app.button2.grid(row=3, column=3, padx=150, pady=20, ipadx=0, ipady=5)
            app.button4 = tk.Button(app.frame1Frame2, bd=2, text ="Mes Reservation", bg='red', fg='black',width=30, height=1, command=mes_reservation)
            app.button4.configure(font=('helvetica', 12))
            app.button4.grid(row=5, column=3, padx=50, pady=20, ipadx=0, ipady=5)
            
            app.button5 = tk.Button(app.frame1Frame2, bd=2, text ="Deconnexion", bg='red', fg='black',width=30, height=1,  command=deconnexion)
            app.button5.configure(font=('helvetica', 12))
            app.button5.grid( row=7, column=1,padx=0, pady=20, ipadx=0, ipady=5)
            
            app.button6 = tk.Button(app.frame1Frame2, bd=2, text ="Profil", bg='red', fg='black',width=30, height=1,  command=lambda: mon_profil(home))
            app.button6.configure(font=('helvetica', 12))
            app.button6.grid( row=7, column=3,padx=0, pady=20, ipadx=0, ipady=5)
            home.mainloop()
            
        elif result == 'Admin':
            
            home = tk.Tk()
            app = Home(home, username)
            app.button1 = tk.Button(app.frame1Frame2, bd=2, text ="Gestion. Utilisateur", bg='red', fg='black',width=30, height=1, state=tk.NORMAL,command=open_ges_users)
            app.button1.configure(font=('helvetica', 12))
            app.button1.grid(row=3, column=1, padx=150, pady=20, ipadx=0, ipady=5)
            app.button3 = tk.Button(app.frame1Frame2, bd=2, text ="Gestion. Evenement", bg='red', fg='black',width=30, height=1,state=tk.NORMAL,command=open_ges_event)
            app.button3.configure(font=('helvetica', 12)) 
            app.button3.grid(row=5, column=1, padx=150, pady=20, ipadx=0, ipady=5)
            app.button2 = tk.Button(app.frame1Frame2, bd=2, text ="Gestion. Reservation", bg='red', fg='black',width=30, height=1, command=open_ges_reservation)
            app.button2.configure(font=('helvetica', 12))
            app.button2.grid(row=3, column=3, padx=150, pady=20, ipadx=0, ipady=5)
            app.button4 = tk.Button(app.frame1Frame2, bd=2, text ="Mes Reservation", bg='red', fg='black',width=30, height=1, command=mes_reservation)
            app.button4.configure(font=('helvetica', 12))
            app.button4.grid(row=5, column=3, padx=50, pady=20, ipadx=0, ipady=5)
            
            app.button5 = tk.Button(app.frame1Frame2, bd=2, text ="Deconnexion", bg='red', fg='black',width=30, height=1,  command=deconnexion)
            app.button5.configure(font=('helvetica', 12))
            app.button5.grid( row=7, column=1,padx=0, pady=20, ipadx=0, ipady=5)
            
            app.button6 = tk.Button(app.frame1Frame2, bd=2, text ="Profil", bg='red', fg='black',width=30, height=1,  command=lambda: mon_profil(home))
            app.button6.configure(font=('helvetica', 12))
            app.button6.grid( row=7, column=3,padx=0, pady=20, ipadx=0, ipady=5)
            home.mainloop()
    
    
    
    
    
     
        
    
    
    
    
                