import tkinter as tk

def fahrenheit_to_celsius() :
    
    try:
      fahrenheit = float(ent_temperature.get().strip())
      celsiu = (fahrenheit - 32) * 5/9
      celsius = round(celsiu ,2)
      lbl_result.config(text=f"{celsius :.1f} °C")
    except ValueError:
      lbl_result.config(text="Erreur")
window =tk.Tk()
window.title (" Convertisseur de température ")

window.resizable(width=False, height=False) #on ne peut pas reduire la fenêtre

frm_entry = tk.Frame (master=window) 
ent_temperature = tk. Entry(master=frm_entry, width=10)

lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}",font=("Arial",16))


ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="\N{RIGHTWARDS BLACK ARROW}", command=fahrenheit_to_celsius) 

lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}",font=("Arial",16),width=10) 

frm_entry.grid(row=0, column=0, padx=10)

btn_convert.grid(row=0, column=1, pady=10)

lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()