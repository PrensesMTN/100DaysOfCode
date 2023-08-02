# Fahrenheit (Fahrenhayt)(°F)
# Santigrat (Celcius)(°C)
# Reaumur (Reomür)(°R)
# Kelvin (°K) 


import tkinter as tk

win = tk.Tk()
from tkinter import ttk
from tkinter import messagebox

win.title("PERSION Temperature Conversion Calculator")
win.geometry("730x220")
win.resizable(False,False)

def clear():
    tempCombo1.set('')
    tempCombo2.set('')
    lbl_res["text"] = f"Results: " 
    entry.delete(first=0, last='end')

def get_index1(*arg):
    # lbl=tk.Label(win, text=" " + str(varCombo1.get()), font=('Helvetica 12')).grid(column=2,row=4) #str(tempCombo1.current()) # index almak için
    return str(tempCombo1.current())
    # return str(varCombo1.get()) # combo üstündeki değeri almak

def get_index2(*arg):
    return str(tempCombo2.current())
    # return str(varCombo2.get())  # combo üstündeki değeri almak



tempCombo1['values'] = ('Fahrenheit (Fahrenhayt)(°F)',
                          ' Santigrat (Celcius)(°C) ',
                          ' Reaumur (Reomür)(°R) ',
                          ' Kelvin (°K)')
  
tempCombo1.grid(column = 1, row = 0,pady=5)
varCombo1.trace('w', get_index1)


tempCombo2['values'] = ('Fahrenheit (Fahrenhayt)(°F)',
                          ' Santigrat (Celcius)(°C) ',
                          ' Reaumur (Reomür)(°R) ',
                          ' Kelvin (°K)')
  
tempCombo2.grid(column = 5, row = 0)
varCombo2.trace('w', get_index2)



temperature = tk.Frame(master=win)
entry = tk.Entry(master=temperature,font=25,width=5)
entry.grid(row=1, column=2,padx=5,pady=5)



from_lbl = tk.Label(text="From:",font=5)
from_lbl.grid(row=0, column=0,padx=20,pady=5)

btn = tk.Button(text="Convert", command=calc,font=25)
btn.grid(row=3, column=5,padx=30)

btn_clr = tk.Button(text="Clear", command=clear,font=25)
btn_clr.grid(row=3, column=1)


lbl_res = tk.Label(text="Results:",font=5)
lbl_res.grid(row=4, column=2,pady=5)

win.mainloop()



