from modules.main.vues.Home import Home
from modules.main.vues.opening import opening
from modules.users.login import Login

#import interfaces.opening as openg
import tkinter as tk

#fenetre principale du profil d'utilisateur

if __name__ == '__main__':
    log_in = [False]
    while log_in[0] == False :
        windows = tk.Tk()
        windows1 = Login(windows)
        windows.mainloop()
        log_in = windows1.login_gui()
    home = tk.Tk()
    app = Home(home)
    home.mainloop()
     
        
    
    
    
    
                