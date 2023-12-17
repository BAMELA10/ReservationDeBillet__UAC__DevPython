import tkinter as Tk
from tkinter import ttk, messagebox
from .models import users
from .connect import connector
def users_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select username, email, phone, status from users")
        return cursor.fetchall()

class listingUser:
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
        
        
        self.label1 = Tk.Label(self.frame0, text="Listing des Utilisateurs", font=("helvetica", 32), bg='black', fg='red')
        self.label1.grid(column=0 , row=0, padx=10, pady=10)
        
        self.champ1 = ttk.Entry(self.frame1, width=25, font=("helvetica", 14))
        self.champ1.grid(column=0 , row=0)
        
        self.rechercher = ttk.Button(self.frame1, text="Rechercher", width=10)
        self.rechercher.grid(column=1 , row=0)
        
        cols = ("username", "email", "phone","status")
        self.data_grid = ttk.Treeview(self.frame2, show="headings",columns=cols, height=20)
        
        for col in cols:
            self.data_grid.column(col, width=250, anchor="center")
            self.data_grid.heading(col, text=col)
        
        
        rows = users_all()
        for row in rows:
            self.data_grid.insert("","end",values=row)
        
        self.data_grid.grid(column=0 , row=0)
        
        
        self.button1 = ttk.Button(self.frame3, text="Ajouter", command=self.open_add_user)
        self.button1.grid(row=3, column=0, padx=10, pady=30)
        self.button2 = ttk.Button(self.frame3, text="Rafraichir", command=self.refresh)
        self.button2.grid(row=3, column=1,padx=10, pady=30)
        self.button3 = ttk.Button(self.frame3, text="Modifier",command=self.open_edit_user)
        self.button3.grid(row=3, column=2,padx=10, pady=30)
        self.button4 = ttk.Button(self.frame3, text="Supprimer",command=self.delete_user_gui)
        self.button4.grid(row=3, column=3,padx=10, pady=30)
    
    def open_add_user(self):
        global form_usc
        form_usc = Tk.Toplevel(self.windows)
        form_usc.title("EventCreation")
        form_usc.geometry("800x600")
        #form_usc.resizable(False, False)
        form_usc.configure(bg="black")
        #form_usc

        #isertion des elements de la fenetre
        frame1 = Tk.Frame(form_usc, relief=Tk.SUNKEN,  width=200, height=625)
        frame1.configure( bg="red")
        frame1.grid(column=1, row=0)
        
        frame2 = Tk.Frame(form_usc, relief=Tk.SUNKEN, width=400, height=600)
        frame2.configure( bg="black")
        frame2.grid(column=2, row=0)
        
        frame3 = Tk.Frame(frame2, relief=Tk.SUNKEN, width=10, height=10)
        frame3.configure( bg="black")
        frame3.grid(column=1, row=0)
        
        frame4 = Tk.Frame(frame2, relief=Tk.SUNKEN, width=150, height=200)
        frame4.configure( bg="black")
        frame4.grid(column=1, row=1)
        #Insertion du titre de la fenetre 
        title = Tk.Label(frame3, text="Creation d'utilisateur")
        title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        title.grid(column=0, row=0, pady=30)
        
        label1 = Tk.Label(frame4, text="Nom de l'utilisateur")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=1)
        global champ_c1
        champ_c1 = Tk.Entry(frame4, width=20, font=("helvetica", 18),)
        champ_c1.grid(column=1, row=1, pady=30)
        
        
        label2 = Tk.Label(frame4, text="Mot de passe", bg="black")
        label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        label2.grid(column=0, row=2)
        global champ_c2
        champ_c2 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ_c2.grid(column=1, row=2, pady=30)
        
        
        label3 = Tk.Label(frame4, text="Statut",bg="black")
        label3.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label3.grid(column=0, row=5)
        global champ_c3
        champ_c3 = ttk.Combobox(frame4, width=10, font=("helvetica", 18), value=["Admin", "Standard"])
        champ_c3.grid(column=1, row=5)
        
        label4 = Tk.Label(frame4, text="Email",bg="black")
        label4.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label4.grid(column=0, row=3)
        global champ_c4
        champ_c4 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ_c4.grid(column=1, row=3, pady=30)
        
        label5 = Tk.Label(frame4, text="Telephone",bg="black")
        label5.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label5.grid(column=0, row=4)
        global champ_c5
        champ_c5 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ_c5.grid(column=1, row=4, pady=30)
        
        btn_validate = Tk.Button(frame4, text="OK",width=15,bg="red", command=self.ajout_user)
        btn_validate.grid(column=0, row=6, pady=50)

        btn_back = Tk.Button(frame4, text="Annuler",width=15, bg="red", command=form_usc.destroy)
        btn_back.grid(column=1, row=6, pady=50)
        
        
    def ajout_user(self):
        connector.ping()
        username = str(champ_c1.get())
        password = str(champ_c2.get())
        status = str(champ_c3.get())
        email = str(champ_c4.get())
        telephone = int(champ_c5.get())
        user = users(username, password, status,  email, telephone)
        user.create_users()
        form_usc.destroy()
        self.refresh()
            
    def refresh(self):
        connector.ping()
        self.windows.destroy()
        rows = users_all()
        fenetre = Tk.Tk()
        fenetre1 = listingUser(fenetre)
        fenetre.mainloop()

            
    def select_item(self):
        user1 = self.data_grid.selection()
        if user1:
            user1_value = self.data_grid.item(user1,"values")
        return user1_value
    
    def open_edit_user(self):
        user1_value = self.select_item()
        global windows1
        windows1 = Tk.Toplevel(self.windows)
        windows1.title("EventEdit")
        windows1.geometry("800x600")
        #windows1.resizable(False, False)
        windows1.configure(bg="black")
        #windows1

        #isertion des elements de la fenetre
        frame1 = Tk.Frame(windows1, relief=Tk.SUNKEN,  width=200, height=625)
        frame1.configure( bg="red")
        frame1.grid(column=1, row=0)
        
        frame2 = Tk.Frame(windows1, relief=Tk.SUNKEN, width=400, height=600)
        frame2.configure( bg="black")
        frame2.grid(column=2, row=0)
        
        frame3 = Tk.Frame(frame2, relief=Tk.SUNKEN, width=10, height=10)
        frame3.configure( bg="black")
        frame3.grid(column=1, row=0)
        
        frame4 = Tk.Frame(frame2, relief=Tk.SUNKEN, width=150, height=200)
        frame4.configure( bg="black")
        frame4.grid(column=1, row=1)
        #Insertion du titre de la fenetre 
        title = Tk.Label(frame3, text="Modification d'utilisateur")
        title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        title.grid(column=0, row=0, pady=30)
        
        label1 = Tk.Label(frame4, text="Nom de l'utilisateur")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=1)
        global champ1
        champ1 = Tk.Entry(frame4, width=20, font=("helvetica", 18),)
        champ1.grid(column=1, row=1, pady=30)
        champ1.insert(0, user1_value[0])
        
        global champ3
        label3 = Tk.Label(frame4, text="Statut",bg="black")
        label3.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label3.grid(column=0, row=5)
        
        champ3 = ttk.Combobox(frame4, width=10, font=("helvetica", 18), value=["Admin", "Standard"])
        champ3.insert(0, user1_value[3])
        champ3.grid(column=1, row=5)
        
        
        label4 = Tk.Label(frame4, text="Email",bg="black")
        label4.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label4.grid(column=0, row=3)
        
        global champ4
        champ4 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ4.insert(0, user1_value[1])
        champ4.grid(column=1, row=3, pady=30)
        
        
        label5 = Tk.Label(frame4, text="Telephone",bg="black")
        label5.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label5.grid(column=0, row=4)
        
        global champ5
        champ5 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ5.insert(0, user1_value[2])
        champ5.grid(column=1, row=4, pady=30)
        
        
        btn_validate = Tk.Button(frame4, text="OK",width=15,bg="red",command=self.edit_user)
        btn_validate.grid(column=0, row=6, pady=50)

        btn_back = Tk.Button(frame4, text="Annuler",width=15, bg="red", command=windows1.destroy)
        btn_back.grid(column=1, row=6, pady=50)
    
    
    def edit_user(self):
        list_value = [
                str(champ1.get()),
                str(champ3.get()),
                str(champ4.get()),
                int(champ5.get())
                                    ]
        user1_value = self.select_item()
        new_data = list_value
        edit_user = users(new_data[0], "", new_data[1], new_data[2], new_data[3])
        result = edit_user.edit_users(user1_value[0])
        if result == True:
            messagebox.showinfo("edit", " success")
        else:
            messagebox.showinfo("edit", " lose operation")
        windows1.destroy()
        self.refresh()
        
        
    def delete_user_gui(self):
        user_value = self.select_item()
        user = users(user_value[0],user_value[1],user_value[2],user_value[2],user_value[3])
        result = user.delete_users()
        print(result)
        if result == True:
            messagebox.showinfo("delete","user deleted")
        else:
            messagebox.showinfo("delete","user not deleted")
        self.refresh()
#fenetre.mainloop()