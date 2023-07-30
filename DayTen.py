import tkinter as tk

def hesapla():
    yetiskin = entry_yetiskin.get()
    cocuk = entry_cocuk.get()
    bebek = entry_bebek.get()
    if yetiskin:
        print(yetiskin)
    else:
        yetiskin = 0
    
    if cocuk:
        print(yetiskin)
    else:
        cocuk = 0
    
    if bebek:
        print(yetiskin)
    else:
        bebek = 0

    sonuc = int(yetiskin)*1250 + int(cocuk)*750 + int(bebek)*500
    lbl_hesapla["text"] = f"{sonuc} Litre"
    print()

win = tk.Tk()


entry_yetiskin = tk.Entry(master=win,font=25)
entry_cocuk = tk.Entry(master=win,font=25)
entry_bebek = tk.Entry(master=win,font=25)


lbl = tk.Label(text="Su ihtiyacı Hesaplama Programı",font=35)

lbl_yetiskin = tk.Label(text="Ailenizdeki yetişkin sayısını giriniz",font=35)
lbl_cocuk = tk.Label(text="Ailenizdeki çocuk sayısını giriniz",font=35)
lbl_bebek = tk.Label(text="Ailenizdeki bebek sayısını giriniz",font=35)

lbl_hesapla = tk.Label(text="",font=35)

btn_hesapla = tk.Button(text="Hesapla",command=hesapla ,font=25)

#widget görüntüleme
lbl.grid(row=0,column=1,padx=10,pady=10)
lbl_yetiskin.grid(row=1,column=0,padx=10,pady=10)
lbl_cocuk.grid(row=1,column=1,padx=10,pady=10)
lbl_bebek.grid(row=1,column=2,padx=10,pady=10)
lbl_hesapla.grid(row=3,column=2,padx=10,pady=10)


entry_yetiskin.grid(row=2,column=0,padx=10,pady=10)
entry_cocuk.grid(row=2,column=1,padx=10,pady=10)
entry_bebek.grid(row=2,column=2,padx=10,pady=10)

btn_hesapla.grid(row=3,column=1,padx=10,pady=10)

win.mainloop()