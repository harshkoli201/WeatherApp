from tkinter import *


app = Tk()
app.title("World Weather")
app.geometry('700x500')
app.configure(bg='blue')

def search():
    pass

city_name = StringVar()
city_entry = Entry(app, textvariable=city_name, width=45)
city_entry.pack(pady=20)

button = Button(app, text = "Search Weather", command=search,  width= 15)
button.pack(pady=10)

location_name = Label(app, text ="", font=('bold',20))
location_name.pack(pady=10)

# image = Label(app, bitmap='')
# image.pack()

Temp_lbl= Label(app, text="")
Temp_lbl.pack(pady=10)

weather = Label(app, text="")
weather.pack(pady=10)


app.mainloop()