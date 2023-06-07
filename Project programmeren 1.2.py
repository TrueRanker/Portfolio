import tkinter as tk
from tkinter import messagebox

Awansersheet = []
geslacht = ["man", "vrouw", "overig"]

def check_geslacht():
    gebruiker_geslacht = geslacht_entry.get().lower()
    if gebruiker_geslacht in geslacht:
        messagebox.showinfo("Geslacht", f"Uw geslacht is {gebruiker_geslacht}")
        Awansersheet.append(gebruiker_geslacht)
    else:
        messagebox.showerror("Ongeldig geslacht", "Het ingevoerde geslacht is ongeldig")

def check_motivatie_zin():
    motivatie_zin = motivatie_entry.get()
    Awansersheet.append(motivatie_zin)

def check_achternaam():
    achternaam = achternaam_entry.get()
    if not achternaam.isalpha():
        messagebox.showerror("Foutieve achternaam", "U heeft een fout gemaakt in uw achternaam.")
    else:
        messagebox.showinfo("Correcte achternaam", "Uw achternaam is correct ingevoerd.")
        Awansersheet.append(achternaam)

def calculate_age():
    birthdate = int(geboortejaar_entry.get())
    current_year = 2023
    age = current_year - birthdate
    messagebox.showinfo("Leeftijd", f"Uw leeftijd is: {age}")
    Awansersheet.append(birthdate)

def check_gegevens():
    messagebox.showinfo("Gegevens", f"Zijn uw gegevens correct ingevoerd? {Awansersheet}")

window = tk.Tk()
window.title("Gebruikersgegevens")

geslacht_label = tk.Label(window, text="Wat is uw geslacht? (man, vrouw of overig)")
geslacht_label.pack()
geslacht_entry = tk.Entry(window)
geslacht_entry.pack()
geslacht_button = tk.Button(window, text="Check", command=check_geslacht)
geslacht_button.pack()

motivatie_label = tk.Label(window, text="Voer hier uw motivatie zin in:")
motivatie_label.pack()
motivatie_entry = tk.Entry(window)
motivatie_entry.pack()
motivatie_button = tk.Button(window, text="Check", command=check_motivatie_zin)
motivatie_button.pack()

achternaam_label = tk.Label(window, text="Wat is uw achternaam?")
achternaam_label.pack()
achternaam_entry = tk.Entry(window)
achternaam_entry.pack()
achternaam_button = tk.Button(window, text="Check", command=check_achternaam)
achternaam_button.pack()

geboortejaar_label = tk.Label(window, text="Voer uw geboortejaar in:")
geboortejaar_label.pack()
geboortejaar_entry = tk.Entry(window)
geboortejaar_entry.pack()
age_button = tk.Button(window, text="Bereken leeftijd", command=calculate_age)
age_button.pack()

gegevens_button = tk.Button(window, text="Check gegevens", command=check_gegevens)
gegevens_button.pack()

window.mainloop()