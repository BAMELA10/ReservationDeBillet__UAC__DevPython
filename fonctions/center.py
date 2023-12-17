def center(root):
    w = root.winfo_vrootwidth() // 2
    h = root.winfo_vrootheight() // 2
    
    # Gets both half the screen width/height and window width/height
    x = (root.winfo_screenwidth() // 2) - (w // 2)
    y = (root.winfo_screenheight() // 2) - (h // 2)

    # Positions the window at the desired location
    root.geometry(f'{w}x{h}+{x}+{y}') 