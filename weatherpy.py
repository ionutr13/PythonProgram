from tkinter import*
import pyowm
import datetime as dt
def change_city():
    city = var.get()
    apikey = "1700fe6cf2c47625cda4e76d881dd56f"
    OpenWMap = pyowm.OWM(apikey)
    city = var.get()
    Weather = OpenWMap.weather_at_place(city)
    Data = Weather.get_weather()
    temp = Data.get_temperature(unit = 'celsius')
    Label(master, text="Average Temp. Currently %s" %temp['temp']).grid(row = 2)
    Label(master, text="Max Temp. Currently %s" %temp['temp_max']).grid(row = 3)
    Label(master, text="Min Temp. Currently %s" %temp['temp_min']).grid(row = 4)

CityList = [
    "Bucharest",
    "London",
    "Paris",
    "Cluj",
    "Botosani",
    "Barcelona",
    "Washington"
]
master = Tk()
master.title("Weather")
master.geometry("500x500")
master.configure(bg = 'lightgray')
Label(master, text="Chose city").grid(row = 0)
var = StringVar()
var.set(CityList[0])
set1 = OptionMenu(master,var,*CityList)
set1.configure(font=("Arial",25))
set1.grid(row = 1, column = 0)


apikey = "1700fe6cf2c47625cda4e76d881dd56f"
OpenWMap = pyowm.OWM(apikey)
city = var.get()
Weather = OpenWMap.weather_at_place(city)
Data = Weather.get_weather()
temp = Data.get_temperature(unit = 'celsius')

Label(master, text="Average Temp. Currently %s" %temp['temp']).grid(row = 2)
Label(master, text="Max Temp. Currently %s" %temp['temp_max']).grid(row = 3)
Label(master, text="Min Temp. Currently %s" %temp['temp_min']).grid(row = 4)
Label(master, text=f"{dt.datetime.now():%a,%b,%d.%Y}", fg= "white", bg="black",font=("halvetica",40)).grid(row=6)
ChangeButton = Button(master,text= "Change",command = change_city).grid(row = 5)


master.mainloop()


