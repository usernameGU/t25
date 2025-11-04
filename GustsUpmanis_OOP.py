import tkinter as tk
from tkinter import messagebox
logs=tk.Tk()

#izveidojam logu
logs.title("Kinētiskās enerģijas kalkulātors")
logs.config(bg="#406642")
logs.geometry("342x250")
logs.minsize(200,200)
logs.maxsize(600,600)
logs.resizable(True,True)

#etiķete
etikete1=tk.Label(logs,text="Ievadi logos masu un ātrumu",
                  bg="white",
                  fg="black",
                  font=("Arial",10,"bold"),
                  padx=40,
                  pady=20,
                  width=20,
                  height=2,
                  justify=tk.CENTER
                  )
etikete1.grid(row=1,column=2)


def izrekinat():
    try:
        # iegūst vērtības no entry laukiem un pārvērš par float
        masa = float(entry1.get())
        atrums = float(entry2.get())
        rezultats = (masa*(atrums*atrums))/2
        rezultats_label.config(text=f"Ķermeņa kinētiskā enerģija ir: {rezultats}N")
    except ValueError:
        messagebox.showerror("Kļūda", "Lūdzu, ievadi derīgus skaitļus!")

#izveido ievades logus
entry1 = tk.Entry(logs)
entry1.grid(row=3,column=2)
#entry1.grid(row=4,column=2)

entry2 = tk.Entry(logs)
entry2.grid(row=4,column=2)

#ievades logu nosaukumi
tk.Label(logs,text="Masa:").grid(row=3, column=1)
tk.Label(logs,text="Ātrums:").grid(row=4,column=1)

#poga "Izrēķināt"
izrekinat_poga = tk.Button(logs, text="Izrēķināt", command=izrekinat)
izrekinat_poga.grid(row=6,column=2)

#Label rezultāta parādīšanai
rezultats_label = tk.Label(logs, text="Ķermeņa kinētiskā enerģija ir:")
rezultats_label.grid(row=7,column=2)



logs.mainloop()