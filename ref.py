from tkinter import *
from tkinter import ttk

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result.set(num1 + num2)
    except ValueError:
        result.set("Invalid input")

def main():
    global entry1, entry2, result  # Declare global variables
    root = Tk()
    root.title("Simple Addition Calculator")
    
    frm = ttk.Frame(root, padding=10)
    frm.grid(sticky=(N, S, E, W))
    
    # Labels and entries for the numbers
    ttk.Label(frm, text="Number 1:").grid(column=0, row=0, sticky=E)
    entry1 = ttk.Entry(frm, width=10)
    entry1.grid(column=1, row=0, sticky=(W, E))
    
    ttk.Label(frm, text="Number 2:").grid(column=0, row=1, sticky=E)
    entry2 = ttk.Entry(frm, width=10)
    entry2.grid(column=1, row=1, sticky=(W, E))
    
    # Result label
    ttk.Label(frm, text="Result:").grid(column=0, row=2, sticky=E)
    result = StringVar()
    ttk.Label(frm, textvariable=result).grid(column=1, row=2, sticky=(W, E))
    
    # Add button
    ttk.Button(frm, text="Add", command=add_numbers).grid(column=0, row=3, columnspan=2)
    
    # Configure grid
    frm.columnconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)
    frm.rowconfigure(0, weight=1)
    frm.rowconfigure(1, weight=1)
    frm.rowconfigure(2, weight=1)
    frm.rowconfigure(3, weight=1)
    
    root.mainloop()

if __name__ == "__main__":
    main()