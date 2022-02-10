from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
from turtle import bgcolor
import requests

app = Tk()
app.title("World Weather")
app.geometry('700x500')
app.config(bg = 'green')

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api = config['api_key']['key']

def search():
    global img
    city = city_entry.get()
    weather = get_weather(city)
    print(weather)
    if weather:
        location_name['text'] = '{}, {}'.format(weather[0],weather[1])
        img['file'] = 'weather_icons\{}@2x.png'.format(weather[4])
        Temp_lbl['text'] = '{:.2f}°C, {:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = weather[5]
    else:
        messagebox.showerror('Error', 'Cannot find City {}'.format(city))

def get_weather(city):
    result = requests.get(url.format(city, api))
    if result:
        json = result.json()
        #(City, Country, temp_celsius, temp_fahrenheit, icon, weather)
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp'] 
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit  = (temp_kelvin - 273.15) * 9 / 5 + 35
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        final = (city, country,temp_celsius,temp_fahrenheit,icon,weather)
        return final
    else:
        return None

        



city_name = StringVar()
city_entry = Entry(app, textvariable=city_name, width=45)
city_entry.pack(pady=20)

button = Button(app, text = "Search Weather", command=search,  width= 15)
button.pack(pady=10)

location_name = Label(app, text ="", font=('bold',20))
location_name.pack(pady=10)

img = PhotoImage(file="")
Image = Label(app, image = img)
Image.pack()

Temp_lbl= Label(app, text="",font=('bold',20))
Temp_lbl.pack(pady=10)

weather_lbl = Label(app, text="",font=('bold',20))
weather_lbl.pack(pady=10)

app.mainloop()