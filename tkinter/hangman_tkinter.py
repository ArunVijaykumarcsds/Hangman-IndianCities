"""
================================================
🇮🇳 HANGMAN - I ❤ My India (Tkinter Edition)
================================================

📌 Description:
A GUI-based Hangman game built with Python's Tkinter library. 
The game challenges players to guess the name of an Indian city, 
one letter at a time, with lives ticking down on wrong guesses.

🎮 Features:
- Clean GUI interface using Tkinter
- Random Indian city word selection
- Validated single-letter input
- Win/loss popup messages
- Simple and educational gameplay

🧑‍💻 Author: Arun vk
📅 Created: 2025
🛠️ Technologies: Python, Tkinter, random, string

🎯 Purpose:
A personal project to practice GUI development and share on professional platforms.

"""

import tkinter as tk
from tkinter import messagebox
import random
import string

# List of Indian cities
words = ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
         "Pune", "Ahmedabad", "Jaipur", "Surat", "Lucknow", "Kanpur", "Bhopal", "Agra", "Indore"]

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("🇮🇳 Hangman - I ❤ My India")
        self.word = random.choice(words).upper()
        self.word_letters = set(self.word)
        self.used_letters = set()
        self.lives = 7

        self.word_display = tk.StringVar()
        self.update_display()

        # UI Elements
        self.label = tk.Label(master, textvariable=self.word_display, font=("Consolas", 24))
        self.label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Consolas", 16))
        self.entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

        self.status = tk.Label(master, text=f"Lives: {self.lives}", font=("Consolas", 14))
        self.status.pack(pady=10)

    def update_display(self):
        display = " ".join([l if l in self.used_letters else "_" for l in self.word])
        self.word_display.set(display)

    def make_guess(self):
        guess = self.entry.get().upper().strip()
        self.entry.delete(0, tk.END)

        if not guess or guess not in string.ascii_uppercase or len(guess) != 1:
            messagebox.showwarning("Invalid Input", "Enter a single valid alphabet letter.")
            return

        if guess in self.used_letters:
            messagebox.showinfo("Oops!", f"You already guessed '{guess}'")
            return

        self.used_letters.add(guess)
        if guess in self.word_letters:
            self.word_letters.remove(guess)
        else:
            self.lives -= 1

        self.update_display()
        self.status.config(text=f"Lives: {self.lives}")

        if not self.word_letters:
            messagebox.showinfo("Victory!", f"You guessed it! 🎉 The city was {self.word}")
            self.master.destroy()
        elif self.lives == 0:
            messagebox.showinfo("Game Over", f"You ran out of lives. 😢 The word was {self.word}")
            self.master.destroy()

# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()