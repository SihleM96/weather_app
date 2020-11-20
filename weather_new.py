from tkinter import*
from tkinter import messagebox


def weather_state() :

    import requests, json

    weather_key = 'b2a0e923e0b5f768b7c6561f0f7398d2'


    url = 'https://api.openweathermap.org/data/2.5/weather'


    name_city = City.get()
    params1 = {'appid': weather_key, 'q': name_city, 'units': 'Metric'}
    response = requests.get(url, params=params1)
    weather = response.json()

    if weather['cod'] != '404':
        y = weather['main']
        temp = y['temp']
        pres = y['pressure']
        humid = y['humidity']
        z = weather['weather']
        weather_desc = z[0]['description']
        Temp.insert(15, str(temp) + "" + 'Degrees')
        Etm.insert(10, str(pres) + "" + 'hPa')
        Humid.insert(15, str(humid) + "" + '%')
        Desc.insert(10, str(weather_desc))
    else:
        messagebox.showerror('Enter a valid City')
        City.delete(0, END)

def clear1():
    City.delete(0, END)
    Temp.delete(0, END)
    Etm.delete(0, END)
    Humid.delete(0,END)
    Desc.delete(0, END)

    City.focus_set()

if __name__ == "__main__":

    #Creating Interface

    widget = Tk()
    widget.geometry('450x180')
    widget.config(bg='grey8')
    widget.title('Weather Forecast')
    widget.columnconfigure(1, weight=1)
    widget.columnconfigure(1, weight=2)

    #Entries

    City = Entry(widget, text='Enter city', width=40).grid(column=1, row=0)
    Temp = Entry(widget, width=40).grid(column=1, row=1)
    Etm = Entry(widget, width=40).grid(column=1, row=4)
    Humid = Entry(widget, width=40).grid(column=1, row=5)
    Desc = Entry(widget, width=40).grid(column=1, row=6)


    #labels

    city_label = Label(widget, text='City', width=20, bg='grey8', fg='white').grid(column=0, row=0)
    temp_label = Label(widget, text='Temperature', width=20, bg='grey8', fg='dark green').grid(column=0, row=1)
    atm_label = Label(widget, text='Atmospheric Pressure', width=20, bg='grey8', fg='white').grid(column=0, row=4)
    humid_label = Label(widget, text='Humidity', width=20, bg='grey8', fg='dark green').grid(column=0, row=5)
    lbl_desc = Label(widget, text='Description', width=20, bg='grey8', fg='white') .grid(column=0, row=6)


    #buttons

    submit_btn = Button(widget, text='Check', width=10, height=1, bg='dark green', fg='white', command=weather_state)
    clear_btn = Button(widget, text=' Clear', width=10, height=1, bg='white', fg='grey8', command=clear1)
    submit_btn.grid(column=1, columnspan=3, row=7), clear_btn.grid(column=1, columnspan=3, row=8)
    widget.mainloop()
