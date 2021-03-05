from tkinter import *


def button_click():
    miles = float(miles_input.get())
    km_converted = round(miles * 1.609, 2)
    label_km.config(text=f"{km_converted}")


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=100, pady=50)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

label1 = Label(text="Miles")
label1.grid(column=2, row=0)

label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="Km")
label3.grid(column=2, row=1)

label_km = Label(text="0")
label_km.grid(column=1, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
