from tkinter import *

def miles_to_kilo():
    miles = float(input.get())
    km = round(miles * 1.609)
    result.config(text=km)


window = Tk()

window.title("Miles To Kilometer Conveter")
window.minsize(width=500, height=300)
window.config(padx=100,pady=100)

#Label
is_equal_to = Label(text="is equal to", font=("Arial", 24, "normal"))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10,pady=10)
result = Label(text="0", font=("Arial", 24, "normal"))
result.grid(column=1, row=1)
result.config(padx=10,pady=10)
km = Label(text="km", font=("Arial", 24, "normal"))
km.grid(column=2, row=1)
km.config(padx=10,pady=10)
miles = Label(text="miles", font=("Arial", 24, "normal"))
miles.grid(column=2, row=0)
miles.config(padx=10,pady=10)

#Button
calculate = Button(text="Calculate", command=miles_to_kilo)
calculate.grid(column=1,row=2)

#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)


window.mainloop()
