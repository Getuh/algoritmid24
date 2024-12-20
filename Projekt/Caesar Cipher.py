import tkinter as tk
from tkinter import ttk, messagebox

letters = "abcdefghijklmnopqrsšzžtuvwõäöüxy"
num_letters = len(letters) #tähestiku pikkus

def encrypt(plaintext, key): #krüpteerib teksti lisades "nihke" ehk key
    ciphertext = "" #tulemus
    for letter in plaintext:
        letter = letter.lower() #täht väiketäheks
        if letter == " ":
            ciphertext += " " #tühik
        else:
            index = letters.find(letter) #leiab tähe
            if index == -1: #kui ei kuulu tähestikku
                ciphertext += letter
            else:
                new_index = (index + key) % num_letters #nihutab õige arvu 
                ciphertext += letters[new_index] 
    return ciphertext

def decrypt(ciphertext, key): #dekrüpteerib teksti 
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
                new_index = (index - key) % num_letters #nihutab teksti tagasi
                plaintext += letters[new_index]
    return plaintext

def process_text():
    try:
        text = input_text.get("1.0", "end").strip() #loeb sisestatud teksti
        key = int(key_entry.get()) #võtab key
        action = action_var.get() #kas dekrüpteerib või krüpteerib

        if not (1 <= key <= num_letters): #kas on lubatud vahemikus
            messagebox.showerror("Viga", f"Nihe peab olema vahemikus 1-{num_letters}.") #kui ei ole siis tuleb teksst
            return
        
        if action == "Krüpteeri": #tegevuse valik ja mis juhtub
            result = encrypt(text, key)
        elif action == "Dekrüpteeri":
            result = decrypt(text, key)
        else:
            result = "Vali tegevus!" #kui tegevus poel valitud aga kasutaja vajutab "töötle"
        
        output_text.delete("1.0", "end")
        output_text.insert("1.0", result)
    except ValueError:
        messagebox.showerror("Viga", "Sisesta korrektne arv nihke jaoks!") #kui key pole antud vahemikus


root = tk.Tk()
root.title("Caesar cipher ")
root.geometry("500x500")
root.configure(bg = "lavender")    

title_label = tk.Label(root, text="CAESAR CIPHER :3 ", fg = "maroon4", font=("Comic Sans MS", 14, "bold"))
title_label.pack(pady=10)
title_label.config(bg = "lavender")

#Sisendi lahter
input_label = tk.Label(root, text="Sisesta tekst:", fg = "maroon4", font=("Comic Sans MS", 10))
input_label.pack(anchor="w", padx=20)
input_text = tk.Text(root, height=5, width=50, wrap="word", font=("Comic Sans MS", 10))
input_text.pack(padx=20, pady=5)
input_label.config(bg = "lavender")
input_text.config(bg="ghostwhite")

#Sisend
key_label = tk.Label(root, text="Sisesta nihe (1-31):", fg = "maroon4", font=("Comic Sans MS", 10))
key_label.pack(anchor="w", padx=20)
key_entry = tk.Entry(root, width=10, font=("Comic Sans MS", 10))
key_entry.pack(padx=20, pady=5)
key_label.config(bg = "lavender")
key_entry.config(bg="ghostwhite")


style = ttk.Style()
style.configure("Custom.TFrame", background="lavender")
style.configure("Custom.TRadiobutton", background="lavender", foreground="maroon4")

#valik
action_var = tk.StringVar(value="Krüpteeri")
action_frame = ttk.Frame(root, style = "Custom.TFrame")
action_frame.pack(pady=10)
action_encrypt = ttk.Radiobutton(action_frame, text="Krüpteeri", variable=action_var, value="Krüpteeri", style="Custom.TRadiobutton")
action_decrypt = ttk.Radiobutton(action_frame, text="Dekrüpteeri", variable=action_var, value="Dekrüpteeri", style="Custom.TRadiobutton")
action_encrypt.pack(side="left", padx=10)
action_decrypt.pack(side="left", padx=10)

#Töötle
process_button = ttk.Button(root, text="Töötle", command=process_text)
process_button.pack(pady=10)


#Tulemus
output_label = tk.Label(root, text="Tulemus:", fg = "maroon4", font=("Comic Sans MS", 10))
output_label.pack(anchor="w", padx=20)
output_text = tk.Text(root, height=5, width=50, wrap="word", font=("Comic Sans MS", 10), state="normal")
output_text.pack(padx=20, pady=5)
output_label.config(bg = "lavender")
output_text.config(bg="ghostwhite")

root.mainloop()