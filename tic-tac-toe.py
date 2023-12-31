from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tic Tac Toe")

# Si 'X' commence, Cliked est True
Clicked = True
count = 0

# Fonction pour désactiver les boutons sur la grille à 9 cases
def disable_button():
    for button in buttons:
        button.config(state=DISABLED)

# Fonction pour déterminer le gagnant
def check_if_win():
    global winner
    winner = False

    # Vérifier case vertical
    for i in range(3):
        if buttons[i * 3]["text"] == buttons[i * 3 + 1]["text"] == buttons[i * 3 + 2]["text"] != "":
            winner = True
            for j in range(3):
                buttons[i * 3 + j].config(bg="green")
            break

    # Vérifier les colonnes 3X3
    for i in range(3):
        if buttons[i]["text"] == buttons[i + 3]["text"] == buttons[i + 6]["text"] != "":
            winner = True
            for j in range(3):
                buttons[i + j * 3].config(bg="green")
            break

    # Vérifier les diagonales
    if buttons[0]["text"] == buttons[4]["text"] == buttons[8]["text"] != "":
        winner = True
        for i in [0, 4, 8]:
            buttons[i].config(bg="green")

    if buttons[2]["text"] == buttons[4]["text"] == buttons[6]["text"] != "":
        winner = True
        for i in [2, 4, 6]:
            buttons[i].config(bg="green")

    if winner:
        messagebox.showinfo("Félicitations", f"Le joueur {buttons[0]['text']} a gagné !")
        disable_button()

# Fonction appelée lorsqu'un bouton est cliqué
def button_click(button):
    global Clicked, count
    if button["text"] == "" and Clicked:
        button["text"] = "X"
        count += 1
        Clicked = False
        check_if_win()
    elif button["text"] == "" and not Clicked:
        button["text"] = "O"
        count += 1
        Clicked = True
        check_if_win()

    if count == 9 and not winner:
        messagebox.showinfo("Match nul", "La partie est un match nul.")
        disable_button()

# Créer les boutons
buttons = []
for i in range(3):
    for j in range(3):
        button = Button(window, text="", font=('normal', 20), height=3, width=6,
                        command=lambda row=i, col=j: button_click(buttons[row * 3 + col]))
        button.grid(row=i, column=j)
        buttons.append(button)

window.mainloop()
