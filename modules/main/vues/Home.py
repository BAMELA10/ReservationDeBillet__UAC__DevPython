#menu
import tkinter as tk
from tkinter import ttk
#import center as ct
class Home:
    def __init__(self, windows,username):
        self.windows = windows
        self.windows.title("Home")
        self.windows.geometry("1272x720")
        #self.windows.resizable(False, False)
        self.windows.configure( bg="black")
        #self.windows

        #isertion des elements de la fenetre
        self.frame1 = tk.Frame(self.windows, relief=tk.SUNKEN,  width=self.windows.winfo_reqwidth(), height=720)
        self.frame1.configure( bg="red")
        self.frame1.grid(row=0, column=1)
        
        self.frame2 = tk.Frame(self.windows, relief=tk.SUNKEN)
        self.frame2.configure( bg="black")
        self.frame2.grid(row=0, column=2, padx=0, pady=0,ipadx=25, ipady=20)
        
        self.frame1Frame2 = tk.Frame(self.frame2, relief=tk.SUNKEN, width=200, height=1)
        self.frame1Frame2.configure(bg="black")
        self.frame1Frame2.grid(row=3, column=2, columnspan=5, padx=0, pady=0,ipadx=0, ipady=30)
        
        self.frame3 = tk.Frame(self.frame2, relief=tk.SUNKEN)
        self.frame3.configure( bg="black")
        self.frame3.grid(row=4, column=2, padx=0, pady=0,ipadx=25, ipady=0)
        
        TEXTE = "MENU"
        self.text2 = tk.Label(self.frame2, bg='black',text=TEXTE, fg='red', width=10, height=2)
        self.text2.configure(font=("helvetica", 30), bd=0, fg='red', bg="black")
        self.text2.grid(row=1, column=2 , padx=100, pady=0, ipadx=290)
        
        TEXTE = "MENU DE SELECTION DES DIFFERENTS OPTION DE L'APPLICATION \n SELECTIONNER UNE OPTION ET EVOLUER DANS VOTRE TACHE "
        self.text1 = tk.Label(self.frame2, bg='black',text=TEXTE, fg='red',width=60, height=5)
        self.text1.configure(font=("helvetica", 14), bd=0)
        self.text1.grid(row=2, column=2 , padx=100, pady=20, ipadx=150, ipady=0)
        
        
        
        self.button1 = tk.Button(self.frame1Frame2, bd=2, text ="Gestion. Utilisateur", bg='red', fg='black',width=30, height=1)
        self.button1.configure(font=('helvetica', 12))
        self.button1.grid(row=3, column=1, padx=150, pady=20, ipadx=0, ipady=5)       
        
        self.button2 = tk.Button(self.frame1Frame2, bd=2, text ="Gestion. Reservation", bg='red', fg='black',width=30, height=1)
        self.button2.configure(font=('helvetica', 12))
        self.button2.grid(row=3, column=3, padx=150, pady=20, ipadx=0, ipady=5)
        
        self.button3 = tk.Button(self.frame1Frame2, bd=2, text ="Gestion. Evenement", bg='red', fg='black',width=30, height=1)
        self.button3.configure(font=('helvetica', 12))
        self.button3.grid(row=5, column=1, padx=150, pady=20, ipadx=0, ipady=5)
        
        self.button4 = tk.Button(self.frame1Frame2, bd=2, text ="Mes Reservation", bg='red', fg='black',width=30, height=1)
        self.button4.configure(font=('helvetica', 12))
        self.button4.grid(row=5, column=3, padx=50, pady=20, ipadx=0, ipady=5)
        
        self.button5 = tk.Button(self.frame1Frame2, bd=2, text ="Deconnexion", bg='red', fg='black',width=30, height=1)
        self.button5.configure(font=('helvetica', 12))
        self.button5.grid( row=7, column=1,padx=0, pady=20, ipadx=0, ipady=5)
        
        self.button6 = tk.Button(self.frame1Frame2, bd=2, text ="Profil", bg='red', fg='black',width=30, height=1)
        self.button6.configure(font=('helvetica', 12))
        self.button6.grid( row=7, column=3,padx=0, pady=20, ipadx=0, ipady=5)
        
        self.username = username
        TEXTE = "Bienvenue {}".format(self.username)
        self.textx = tk.Label(self.frame3, bg='black',text=TEXTE, fg='red',width=60, height=5)
        self.textx.configure(font=("helvetica", 14), bd=0)
        self.textx.grid(row=0, column=0, padx=100, pady=10, ipadx=20, ipady=0)
        
        
''' fenetre = tk.Tk()
fenetre1 = Home(fenetre)
fenetre.mainloop() '''