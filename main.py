from tkinter import *
from tkinter import ttk
import subprocess
import os

def run_script():
    #subprocess.run(["cmd", "/c", "cd o:\\ && tree"])
    cmd_path = os.path.expandvars(r"%SystemRoot%\system32\cmd.exe")

# Run the command
    subprocess.run([cmd_path])

def main():
    root = Tk()
    root.title("Test Script")
    icon = PhotoImage(file='icon.png')  # Use .ico for best compatibility
    root.iconphoto(False, icon)
    frm = ttk.Frame(root, padding=10)
    frm.grid(sticky=(N, S, E, W))
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 11, "bold"), padding=(40, 10))

    ttk.Label(frm, text="Clock test", anchor="center", font=("Helvetica", 12, "bold")).grid(column=1, row=0,columnspan=3  ,sticky=(W,E))
    
    ttk.Button(frm, text="Run Test", style="TButton", command=run_script, padding=(40, 10)).grid(column=1, row=1, columnspan=3, padx=5, pady=5)
    


    root.mainloop()


if __name__ == "__main__":
    main()