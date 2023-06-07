import tkinter as tk

# def functie berekent de omtrek door middel van de input van de zijdes van het vierkant
# 
def calculate():
    zijde = float(entry_zijde.get())
    omtrek = 4 * zijde
    oppervlakte = zijde * zijde
    lbl_omtrek["text"] = f"De omtrek van het vierkant is: {omtrek}"
    lbl_oppervlakte["text"] = f"De oppervlakte van het vierkant is: {oppervlakte}"


# Tkinter code om een widow te openen waar je de zijde kan invoeren
# Hieronder staat hoe groot de aplicatie is op je scherm
# Button die ervoor zorgt dat je op berekenen kan klikken 
root = tk.Tk()
root.title("Bereken vierkant")
root.geometry("300x150")

lbl_zijde = tk.Label(root, text="Voer de zijde van het vierkant in:")
lbl_zijde.pack()

entry_zijde = tk.Entry(root)
entry_zijde.pack()

btn_bereken = tk.Button(root, text="Bereken", command=calculate)
btn_bereken.pack()

lbl_omtrek = tk.Label(root, text="")
lbl_omtrek.pack()

lbl_oppervlakte = tk.Label(root, text="")
lbl_oppervlakte.pack()

# root.mainloop zorgt ervoor dat de aplicatie opent en open blijft
root.mainloop()