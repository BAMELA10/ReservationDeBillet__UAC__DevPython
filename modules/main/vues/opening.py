import tkinter as tk
#import center as ct

class opening:
    def __init__(self, windows):
        self.windows = windows
        self.windows.title("opening")
        self.windows.overrideredirect(1)
        self.windows.geometry("500x200")
        self.windows.resizable(False, False)
        self.windows.configure(bg = "black")
        #self.windows

        #insertion du texte d ' opening dans la fenetre 
        self.frame1 = tk.Frame(self.windows, bd=0, relief=tk.SUNKEN,  width=100, height=100)
        self.label1 = tk.Label(self.frame1, fg="red", text="Welcome To The Event App")
        self.label1.config(font = ('times new roman', 40),bg = "black")
        self.frame1.pack(expand=True)
        self.label1.pack(expand=True)


windows = tk.Tk()
windows1 = opening(windows)
#ct.center(windows)
windows.mainloop()