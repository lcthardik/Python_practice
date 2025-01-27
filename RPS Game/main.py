from tkinter import *
from tkinter import ttk
import random

options=['r','p','s']
user_points=0
computer_points=0

def play(x):
    global win_stat,pc_score,user_score,user_points, computer_points, name
    #print("lets play")
    pc=random.choice(options)
    if x==pc:
        win_stat.set('Draw')
    elif ((pc=='r' and x=='s') or (pc=='p' and x=='r') or (pc=='s' and x=='p')):
        #output='Computer Wins'
        win_stat.set('Computer Wins')
        computer_points+=1
    else:
        #output='User Wins'
        win_stat.set(name+' Wins')
        user_points+=1
    user_score.set(str(user_points))
    pc_score.set(str(computer_points))
    #print(user_points)
    #print(computer_points)


def rock():
    #print("rock")
    play('r')
def paper():
    play('p')
def scissor():
    play('s')


def main():
    global win_stat,pc_score,user_score,name
    name=input("Enter player name: ")
    name+=": "
    
    root = Tk()
    root.title("RPS Game")
    icon = PhotoImage(file='icon.png')  # Use .ico for best compatibility
    root.iconphoto(False, icon)
    frm = ttk.Frame(root, padding=10)
    frm.grid(sticky=(N, S, E, W))

    user_score = StringVar()
    pc_score = StringVar()
    win_stat=StringVar()
    

    ttk.Label(frm, text="RPS Game!!!", anchor="center", font=("Helvetica", 12, "bold")).grid(column=1, row=0,columnspan=3  ,sticky=(W,E))
    
    ttk.Button(frm, text="Rock", command=rock, padding=(6, 3)).grid(column=1, row=1, padx=5, pady=5)
    ttk.Button(frm, text="Paper", command=paper, padding=(6, 3)).grid(column=2, row=1, padx=5, pady=5)
    ttk.Button(frm, text="Scissor", command=scissor, padding=(6, 3)).grid(column=3, row=1, padx=5, pady=5)
    
    ttk.Label(frm, text="Score", font=("Helvetica", 12, "bold")).grid(column=1, row=2, sticky=W)
    ttk.Label(frm, text=name,font=("Helvetica", 10)).grid(column=2, row=2, sticky=W)
    ttk.Label(frm, textvariable=user_score).grid(column=2, row=2)
    ttk.Label(frm, text="PC:", font=("Helvetica", 10)).grid(column=3, row=2, sticky=W)
    ttk.Label(frm, textvariable=pc_score).grid(column=3, row=2)
    ttk.Label(frm, textvariable=win_stat,font=("Helvetica", 11, "bold")).grid(column=1, row=3,sticky=W, columnspan=2)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=4, padx=5, pady=5)
    #result = StringVar()
    #ttk.Label(frm, textvariable=result).grid(column=1, row=2, sticky=(W, E))
    #x=4
    #y=5

    #user_score.set(str(user_points))
    #pc_score.set(str(computer_points))
    #win_stat.set(output)


    root.mainloop()


if __name__ == "__main__":
    main()