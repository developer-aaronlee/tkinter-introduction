from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

input = Entry(width=10)
input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

is_label = Label(text="is equal to")
is_label.grid(column=0, row=1)

output = Label(text="0")
output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

def calc():
    user_input = float(input.get())
    outcome = round(user_input * 1.6)
    output.config(text=f"{outcome}")

button = Button(text="Calculate", command=calc)
button.grid(column=1, row=2)






window.mainloop()