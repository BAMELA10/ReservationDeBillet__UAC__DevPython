#fenetre de connexion du user
#fenetre de creation du user
import tkinter as tk
#import center as ct
class EventCreation:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("EventCreation")
        self.windows.geometry("800x600")
        self.windows.resizable(False, False)
        self.windows.configure(bg="black")
        #self.windows

        #isertion des elements de la fenetre
        self.frame1 = tk.Frame(self.windows, relief=tk.SUNKEN,  width=200, height=600)
        self.frame1.configure( bg="red")
        self.frame1.grid(column=1, row=0)
        
        self.frame2 = tk.Frame(self.windows, relief=tk.SUNKEN, width=400, height=600)
        self.frame2.configure( bg="black")
        self.frame2.grid(column=2, row=0)
        
        self.frame3 = tk.Frame(self.frame2, relief=tk.SUNKEN, width=10, height=10)
        self.frame3.configure( bg="black")
        self.frame3.grid(column=1, row=0)
        
        self.frame4 = tk.Frame(self.frame2, relief=tk.SUNKEN, width=150, height=200)
        self.frame4.configure( bg="black")
        self.frame4.grid(column=1, row=1)
        
        
        
        
        
        #Insertion du titre de la fenetre 
        self.title = tk.Label(self.frame3, text="Creation d'Evenement")
        self.title.configure(font=("helvetica", 14), width=25,fg= "red",bg="black")
        self.title.grid(column=0, row=0, pady=60)
        
        self.label1 = tk.Label(self.frame4, text="Intitulé de Evenement")
        self.label1.configure(font=("helvetica", 14), width=25,fg= "red" ,bg="black")
        self.label1.grid(column=0, row=1)
        
        self.champ1 = tk.Entry(self.frame4, width=20, font=("helvetica", 18),)
        self.champ1.grid(column=1, row=1, pady=30)
        
        
        self.label2 = tk.Label(self.frame4, text="Date de l'evenement", bg="black")
        self.label2.configure(font=("helvetica", 14), width=25,fg= "red" )
        self.label2.grid(column=0, row=2)
        
        self.champ2 = tk.Entry(self.frame4, width=20, font=("helvetica", 18))
        self.champ2.grid(column=1, row=2, pady=30)
        
        
        self.label3 = tk.Label(self.frame4, text=" Nombres de places",bg="black")
        self.label3.configure(font=("helvetica", 14), bd=5, width=25,fg= "red" )
        self.label3.grid(column=0, row=3)
        
        self.champ3 = tk.Entry(self.frame4, width=20, font=("helvetica", 18))
        self.champ3.grid(column=1, row=3, pady=30)
        
        self.btn_validate = tk.Button(self.frame4, text="OK",width=15,bg="red")
        self.btn_validate.grid(column=0, row=5, pady=50)

        self.btn_back = tk.Button(self.frame4, text="Annuler",width=15, bg="red")
        self.btn_back.grid(column=1, row=5, pady=50)



windows = tk.Tk()
windows1 = EventCreation(windows)
#ct.center(windows)
windows.mainloop()