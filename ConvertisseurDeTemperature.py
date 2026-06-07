{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7bb3958c-9ccc-40e1-b184-f43a236050a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "\n",
    "def fahrenheit_to_celsius() :\n",
    "    \n",
    "    try:\n",
    "      fahrenheit = float(ent_temperature.get().strip())\n",
    "      celsiu = (fahrenheit - 32) * 5/9\n",
    "      celsius = round(celsiu ,2)\n",
    "      lbl_result.config(text=f\"{celsius :.1f} °C\")\n",
    "    except ValueError:\n",
    "      lbl_result.config(text=\"Erreur\")\n",
    "window =tk.Tk()\n",
    "window.title (\" Convertisseur de température \")\n",
    "\n",
    "window.resizable(width=False, height=False) #on ne peut pas reduire la fenêtre\n",
    "\n",
    "frm_entry = tk.Frame (master=window) \n",
    "ent_temperature = tk. Entry(master=frm_entry, width=10)\n",
    "\n",
    "lbl_temp = tk.Label(master=frm_entry, text=\"\\N{DEGREE FAHRENHEIT}\",font=(\"Arial\",16))\n",
    "\n",
    "\n",
    "ent_temperature.grid(row=0, column=0, sticky=\"e\")\n",
    "lbl_temp.grid(row=0, column=1, sticky=\"w\")\n",
    "\n",
    "btn_convert = tk.Button(master=window, text=\"\\N{RIGHTWARDS BLACK ARROW}\", command=fahrenheit_to_celsius) \n",
    "\n",
    "lbl_result = tk.Label(master=window, text=\"\\N{DEGREE CELSIUS}\",font=(\"Arial\",16),width=10) \n",
    "\n",
    "frm_entry.grid(row=0, column=0, padx=10)\n",
    "\n",
    "btn_convert.grid(row=0, column=1, pady=10)\n",
    "\n",
    "lbl_result.grid(row=0, column=2, padx=10)\n",
    "\n",
    "window.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16a11121-bfbe-46a6-8244-6387c66f9c25",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f31ba8ed-2e35-4703-a5ce-d95fc354ffd1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
