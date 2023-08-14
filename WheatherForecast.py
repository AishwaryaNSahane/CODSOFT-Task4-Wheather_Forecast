import tkinter as tk
import requests
import time
from PIL import Image, ImageTk

def getWeather():
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=80d883919bd975df010a2e6638fd2a33"
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C" 
    final_data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")


screen_width = canvas.winfo_screenwidth()
screen_height = canvas.winfo_screenheight()

bg_image = Image.open("th.jpeg")
bg_image = bg_image.resize((screen_width, screen_height))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(canvas, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

heading_label = tk.Label(canvas, text="Weather Forecast", font=("poppins", 24, "bold"), bg="pink",fg="darkblue")
heading_label.pack(pady=5)


user_label = tk.Label(canvas, text="Enter City Name:", bg="white", font=("arial", 18), border="2px solid black")
user_label.pack(pady=5)

textField = tk.Entry(canvas, justify='left', width=10, font=("arial", 28, "bold"))
textField.pack(pady=5)
textField.focus()

canvas.submit_button = tk.Button(canvas, text="Show Weather", font=("Arial", 14, "bold"), bg="green", fg="black", command=getWeather)
canvas.submit_button.pack(pady=5)

label1 = tk.Label(canvas, font=("arial", 18, "bold"))
label1.pack()
label2 = tk.Label(canvas, font=("arial",18, "bold"))
label2.pack()

canvas.mainloop()
