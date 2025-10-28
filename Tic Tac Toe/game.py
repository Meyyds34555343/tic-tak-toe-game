import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x430")

current_player = "X"
buttons = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
root.configure(bg="#f5f6fa")

title_label = tk.Label(root, text="Tic-Tac-Toe", font=("Arial", 22, "bold"), bg="#f5f6fa", fg="#2f3640")
title_label.pack(pady=20)

frame = tk.Frame(root, bg="#f5f6fa")
frame.pack()

status_label = tk.Label(root, text="Player X's Turn", font=("Arial", 14), bg="#f5f6fa", fg="#273c75")
status_label.pack(pady=10)

def check_winner():

    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def on_click(r, c):

    global current_player
    if buttons[r][c]["text"] == "":
        buttons[r][c]["text"] = current_player
        buttons[r][c]["fg"] = "#e84118" if current_player == "X" else "#0097e6"
    if check_winner():
        messagebox.showinfo("Game Over", f"Player {current_player} wins")
        reset_board()
    else:
        draw = True
        for i in range(3):
            for j in range(3):
                if buttons[i][j]["text"] == "":
                    draw = False
                    break
            if not draw:
                break

        if draw:
            messagebox.showinfo("Game Over", "It's a Draw")
            reset_board()
        else:
            current_player = "O" if current_player == "X" else "X"
            status_label.config(text=f"Player {current_player}'s Turn")

def reset_board():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
    status_label.config(text="Player X's Turn")

for r in range(3):
    for c in range(3):
        btn = tk.Button(
            frame, text="", font=("Arial", 20, "bold"),
            width=3, height=1, bg="#dcdde1", fg="#2f3640",
            activebackground="#718093",
            command=lambda r=r, c=c: on_click(r, c)
        )
        btn.grid(row=r, column=c, padx=5, pady=5)
        buttons[r][c] = btn

reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12, "bold"),
                      bg="#44bd32", fg="white", width=12, height=1,
                      command=reset_board)
reset_btn.pack(pady=10)

root.mainloop()
