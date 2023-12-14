import tkinter as tk
#import center as ct

class opening:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("opening")
        self.windows.overrideredirect(1)
        self.windows.geometry("1000x200")
        self.windows.resizable(False, False)
        self.windows.configure(bg = "black")
        #self.windows

        #insertion du texte d ' opening dans la fenetre 
        self.frame1 = tk.Frame(self.windows, bd=0, relief=tk.SUNKEN,  width=100, height=100)
        self.label1 = tk.Label(self.frame1, fg="red", text="Welcome To The Reservation App")
        self.label1.config(font = ('times new roman', 40),bg = "black")
        self.frame1.pack(expand=True)
        self.label1.pack(expand=True)
        
    def center(self):
        w = 1000
        h = 200

        # Gets both half the screen width/height and window width/height
        x = (root.winfo_screenwidth() // 2) - (w // 2)
        y = (root.winfo_screenheight() // 2) - (h // 2)

            # Positions the window at the desired location
        root.geometry(f'{w}x{h}+{x}+{y}')

