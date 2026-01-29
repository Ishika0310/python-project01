from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")

turn = "X"
count = 0
buttons = []

# ---------- FUNCTIONS ----------

def click(i):
    global turn, count

    if buttons[i]["text"] == " ":
        buttons[i]["text"] = turn
        count += 1

        if check_win():
            tkinter.messagebox.showinfo("Tic Tac Toe", turn + " Wins!")
            disable()
        elif count == 9:
            tkinter.messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
        else:
            turn = "O" if turn == "X" else "X"
    else:
        tkinter.messagebox.showinfo("Tic Tac Toe", "Button already clicked!")

def check_win():
    win = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != " ":
            return True
    return False

def disable():
    for b in buttons:
        b.config(state=DISABLED)

# ---------- BUTTONS ----------

for row in range(3):
    for col in range(3):
        btn = Button(tk, text=" ", font="Times 20 bold",
                     width=6, height=3,
                     command=lambda i=len(buttons): click(i))
        btn.grid(row=row, column=col)
        buttons.append(btn)

tk.mainloop()
