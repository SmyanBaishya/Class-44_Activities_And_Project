import tkinter as tk
from tkinter import Label, Button
import random

# Function to determine winner
def play(choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    # Update text labels
    user_label.config(text=f"You chose: {choice}")
    computer_label.config(text=f"Computer chose: {computer_choice}")

    # Update images
    if choice == "Rock":
        user_img_label.config(image=rock_png)

    elif choice == "Paper":
        user_img_label.config(image=paper_png)

    else:
        user_img_label.config(image=scissors_png)

    if computer_choice == "Rock":
        computer_img_label.config(image=rock_png)

    elif computer_choice == "Paper":
        computer_img_label.config(image=paper_png)

    else:
        computer_img_label.config(image=scissors_png)

    # Determine the winner

    if choice == computer_choice:
        result_label.config(text="It's a Tie!", fg="blue")

    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):

        result_label.config(text="You Win!", fg="green")

    else:

     result_label.config(text="Computer Wins!", fg="red")

# Tkinter window setup
root = tk.Tk()
root.title("Rock Paper Scissors App")
root.geometry("400x400")

# Load images
rock_png = tk.PhotoImage(file="rock.png")
paper_png = tk.PhotoImage(file="paper.png")
scissors_png = tk.PhotoImage(file="scissors.png")

# Labels
user_label = Label(root, text="Your choice: ", font=("Arial", 12))
user_label.pack()

computer_label = Label(root, text="Computer's choice: ", font=("Arial", 12))
computer_label.pack()

result_label = Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack()

# Image labels
user_img_label = Label(root)
user_img_label.pack()

computer_img_label = Label(root)
computer_img_label.pack()

# Buttons
rock_button = Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(side="left", padx=10, pady=10)

paper_button = Button(root, text="Paper", command=lambda: play("Paper"))
paper_button.pack(side="left", padx=10, pady=10)

scissors_button = Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(side="left", padx=10, pady=10)

# Run Tkinter loop

root.mainloop()

