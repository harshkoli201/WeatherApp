from tkinter import *


app = Tk()
app.title("World Weather")
app.geometry('700x500')
app.configure(bg='grey')

city_name = StringVar()
city_entry = Entry(app, textvariable=city_name, width=50)
city_entry.pack()












app.mainloop()