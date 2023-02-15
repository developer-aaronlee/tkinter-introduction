from tkinter import *

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = Label(text="This is a label", font=("Arial", 24))
# label.pack()
# label.place(x=200, y=100)
label.grid(column=0, row=0)

label["text"] = "New Text"
# label.config(text="TEXT")

def button_clicked():
    user_input = input.get()
    label.config(text=user_input)

button = Button(text="Click Here", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="Click New Button")
new_button.grid(column=2, row=0)

input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)





window.mainloop()