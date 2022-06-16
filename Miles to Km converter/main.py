from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=150, pady=150)

# my_label = Label(text="New Text", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)
# my_label.config(padx=100, pady=100)
#
# def button_clicked():
#     my_label.config(text=f"{input.get()}")
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=2, row=2)
#
# # New Buttton
# new_button = Button(text="Don't click me")
# new_button.grid(column=3, row=1)
#
# # Entry
# input = Entry(width=20)
# input.grid(column=4, row=3)
# print(input.get())


is_equal_to_label = Label(text="is equal to", font=("Arial", 24, "bold"))
is_equal_to_label.grid(column=0, row=1)

input = Entry(width=40)
input.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column=2, row=0)

zero = Label(text="0", font=("Arial", 24, "bold"))
zero.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 24, "bold"))
km.grid(column=2, row=1)

def button_clicked():
    miles = (text=f"{input.get()}")
    km = miles * 0.6
    return km

calculate_button = Button("Calculate", button_clicked)

mainloop()