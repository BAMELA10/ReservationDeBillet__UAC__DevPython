import tkinter as Tk
from tkinter import ttk, messagebox
import models
from connect import connector
import tkcalendar as tkc
def event_all():
        connector.ping()
        cursor = connector.cursor()
        cursor.execute("select code, intitulé, date_event, number_place from event")
        return cursor.fetchall()
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
        
        cols = ("Code", "Intitulé", "Date de l'evenement", "Nombre de place")
        self.data_grid = ttk.Treeview(self.frame2, show="headings",columns=cols, height=20)
        
        for col in cols:
            self.data_grid.column(col, width=190, anchor="center")
            self.data_grid.heading(col, text=col)
        rows = event_all()
        for row in rows:
            self.data_grid.insert("","end",value=row)
        self.data_grid.grid(column=0 , row=0)
        
        self.button1 = ttk.Button(self.frame3, text="Ajouter", command=self.open_create_event)
        self.button1.grid(row=3, column=0, padx=10, pady=30)
        self.button2 = ttk.Button(self.frame3, text="Rafraichir", command=self.refresh)
        self.button2.grid(row=3, column=1,padx=10, pady=30)
        self.button3 = ttk.Button(self.frame3, text="Modifier", command=self.open_edit_event)
        self.button3.grid(row=3, column=2,padx=10, pady=30)
        self.button4 = ttk.Button(self.frame3, text="Supprimer", command=self.delete_event_gui)
        self.button4.grid(row=3, column=3,padx=10, pady=30)
        
    def refresh(self):
        connector.ping()
        self.windows.destroy()
        rows = event_all()
        fenetre = Tk.Tk()
        fenetre1 = listingEvenement(fenetre)
        fenetre.mainloop()    
        
    def ajout_event(self):
        connector.ping()
        intitule = str(champ_c1.get())
        data_event = str(champ_c2.get_date())
        number_place = str(champ_c3.get())
        event = models.event(intitule, number_place,"",  data_event)
        event.create_event()
        windows1.destroy()
        self.refresh()
         
    def select_item(self):
        event1 = self.data_grid.selection()
        if event1:
            event1_value = self.data_grid.item(event1,"values")
        return event1_value
    
    def open_create_event(self):
        global windows1
        windows1 = Tk.Toplevel(self.windows)
        windows1.title("EventCreation")
        windows1.geometry("800x600")
        windows1.resizable(False, False)
        windows1.configure(bg="black")
        #windows1

        #isertion des elements de la fenetre
        frame1 = Tk.Frame(windows1, relief=Tk.SUNKEN,  width=200, height=600)
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
        title = Tk.Label(frame3, text="Creation d'Evenement")
        title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        title.grid(column=0, row=0, pady=40)
        
        labelx = Tk.Label(frame4, text="Code de Evenement")
        labelx.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        labelx.grid(column=0, row=0)
        global champ_cx
        champ_cx = Tk.Entry(frame4, width=20, font=("helvetica", 18),state="disable", bg="#D3D3D3")
        champ_cx.grid(column=1, row=0, pady=30)
        
        label1 = Tk.Label(frame4, text="Intitulé de Evenement")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=1)
        global champ_c1
        champ_c1 = Tk.Entry(frame4, width=20, font=("helvetica", 18),)
        champ_c1.grid(column=1, row=1, pady=30)
        
        
        label2 = Tk.Label(frame4, text="Date de l'evenement", bg="black")
        label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        label2.grid(column=0, row=2)
        global champ_c2
        champ_c2 = tkc.DateEntry(frame4, width=20, font=("helvetica", 18))
        champ_c2.grid(column=1, row=2, pady=30)
        
        
        label3 = Tk.Label(frame4, text=" Nombres de places",bg="black")
        label3.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label3.grid(column=0, row=3)
        global champ_c3
        champ_c3 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ_c3.grid(column=1, row=3, pady=30)
        
        btn_validate = Tk.Button(frame4, text="OK",width=15,bg="red",command=self.ajout_event)
        btn_validate.grid(column=0, row=5, pady=50)

        btn_back = Tk.Button(frame4, text="Annuler",width=15, bg="red",command=windows1.destroy)
        btn_back.grid(column=1, row=5, pady=50)
        
    def open_edit_event(self):
        global windows2
        windows2 = Tk.Toplevel(self.windows)
        windows2.title("EventEdit")
        windows2.geometry("800x600")
        windows2.resizable(False, False)
        windows2.configure(bg="black")
        #windows2

        #isertion des elements de la fenetre
        frame1 = Tk.Frame(windows2, relief=Tk.SUNKEN,  width=200, height=600)
        frame1.configure( bg="red")
        frame1.grid(column=1, row=0)
        
        frame2 = Tk.Frame(windows2, relief=Tk.SUNKEN, width=400, height=600)
        frame2.configure( bg="black")
        frame2.grid(column=2, row=0)
        
        frame3 = Tk.Frame(frame2, relief=Tk.SUNKEN, width=10, height=10)
        frame3.configure( bg="black")
        frame3.grid(column=1, row=0)
        
        frame4 = Tk.Frame(frame2, relief=Tk.SUNKEN, width=150, height=200)
        frame4.configure( bg="black")
        frame4.grid(column=1, row=1)

        #Insertion du titre de la fenetre 
        title = Tk.Label(frame3, text="Modification d'Evenement")
        title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        title.grid(column=0, row=0, pady=40)
        
        labelx = Tk.Label(frame4, text="Code de Evenement")
        labelx.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        labelx.grid(column=0, row=0)
        
        data = self.select_item() 
        
        global champ_ex
        champ_ex = Tk.Entry(frame4, width=20, font=("helvetica", 18),state="disable", bg="#D3D3D3")
        champ_ex.insert(0, data[0])
        champ_ex.grid(column=1, row=0, pady=30)
        
        label1 = Tk.Label(frame4, text="Intitulé de Evenement")
        label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        label1.grid(column=0, row=1)
        
        global champ_e1
        champ_e1 = Tk.Entry(frame4, width=20, font=("helvetica", 18),)
        champ_e1.insert(0, data[1])
        champ_e1.grid(column=1, row=1, pady=30)
        
        
        label2 = Tk.Label(frame4, text="Date de l'evenement", bg="black")
        label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        label2.grid(column=0, row=2)
        global champ_e2
        champ_e2 = tkc.DateEntry(frame4, width=20, font=("helvetica", 18))
        champ_e2.grid(column=1, row=2, pady=30)
        
        
        label3 = Tk.Label(frame4, text=" Nombres de places",bg="black")
        label3.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        label3.grid(column=0, row=3)
        global champ_e3
        champ_e3 = Tk.Entry(frame4, width=20, font=("helvetica", 18))
        champ_e3.insert(0, data[3])
        champ_e3.grid(column=1, row=3, pady=30)
        
        btn_validate = Tk.Button(frame4, text="OK",width=15,bg="red", command=self.edit_event)
        btn_validate.grid(column=0, row=5, pady=50)

        btn_back = Tk.Button(frame4, text="Annuler",width=15, bg="red", command=windows2.destroy)
        btn_back.grid(column=1, row=5, pady=50)
    
    
    def edit_event(self):
        list_value = [
                str(champ_e1.get()),
                int(champ_e3.get()),
                str(champ_e2.get_date()),
                                    ]
        print(list_value)
        event1_value = self.select_item()
        new_data = list_value
        edit_event = models.event(new_data[0],new_data[1],"", new_data[2])
        result = edit_event.edit_event(event1_value[1])
        if result == True:
            messagebox.showinfo("edit", " success")
        else:
            messagebox.showinfo("edit", " lose operation")
        windows2.destroy()
        self.refresh()
    
    def delete_event_gui(self):
        event_value = self.select_item()
        event = models.event(event_value[1],event_value[1],event_value[0],event_value[2])
        result = event.delete_event()
        print(result)
        if result == True:
            messagebox.showinfo("delete","event deleted")
        else:
            messagebox.showinfo("delete","event not deleted")
        self.refresh()
          
        
fenetre = Tk.Tk()
fenetre1 = listingEvenement(fenetre)
fenetre.mainloop()
         