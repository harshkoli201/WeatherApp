from tkinter import *


app = Tk()
app.title("World Weather")
app.geometry('700x500')
app.configure(bg='blue')

city_name = StringVar()
city_entry = Entry(app, textvariable=city_name, width=45)
city_entry.pack(pady=20)

button = Button(app, text = "Search Weather", width= 15)
button.pack(pady=10)









app.mainloop()