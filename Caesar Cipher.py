import tkinter as tk
from tkinter import ttk, messagebox

letters = "abcdefghijklmnopqrsšzžtuvwõäöüxy"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter == " ":
            ciphertext += " "
        else:
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = (index + key) % num_letters
                ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if letter == " ":
            plaintext += " "
        else:
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = (index - key) % num_letters
                plaintext += letters[new_index]
    return plaintext

def process_text():
    try:
        text = input_text.get("1.0", "end").strip()
        key = int(key_entry.get())
        action = action_var.get()

        if not (1 <= key <= num_letters):
            messagebox.showerror("Viga", f"Võti peab olema vahemikus 1-{num_letters}.")
            return
        
        if action == "Krüpteeri":
            result = encrypt(text, key)
        elif action == "Dekrüpteeri":
            result = decrypt(text, key)
        else:
            result = "Vali tegevus!"
        
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
    except ValueError:
        messagebox.showerror("Viga", "Sisesta korrektne arv võtme jaoks!")


root = tk.Tk()
root.title("Caesar cipher ")
root.geometry("500x400")
root.resizable(False, False)

title_label = tk.Label(root, text="CAESAR CIPHER ", font=("Arial", 13, "bold"))
title_label.pack(pady=10)

#Sisendi lahter
input_label = tk.Label(root, text="Sisesta tekst:", font=("Arial", 9))
input_label.pack(anchor="w", padx=20)
input_text = tk.Text(root, height=5, width=50, wrap="word", font=("Arial", 9))
input_text.pack(padx=20, pady=5)

#Sisend
key_label = tk.Label(root, text="Sisesta võti (1-31):", font=("Arial", 9))
key_label.pack(anchor="w", padx=20)
key_entry = tk.Entry(root, width=10, font=("Arial", 9))
key_entry.pack(padx=20, pady=5)

#valik
action_var = tk.StringVar(value="Krüpteeri")
action_frame = ttk.Frame(root)
action_frame.pack(pady=10)
action_encrypt = ttk.Radiobutton(action_frame, text="Krüpteeri", variable=action_var, value="Krüpteeri")
action_decrypt = ttk.Radiobutton(action_frame, text="Dekrüpteeri", variable=action_var, value="Dekrüpteeri")
action_encrypt.pack(side="left", padx=10)
action_decrypt.pack(side="left", padx=10)

#Töötle
process_button = ttk.Button(root, text="Töötle", command=process_text)
process_button.pack(pady=10)

#Tulemus
output_label = tk.Label(root, text="Tulemus:", font=("Arial", 9))
output_label.pack(anchor="w", padx=20)
output_text = tk.Text(root, height=5, width=50, wrap="word", font=("Arial", 9), state="normal")
output_text.pack(padx=20, pady=5)

root.mainloop()