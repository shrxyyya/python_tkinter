from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root=Tk()
#root.geometry("400x40")
root.title("Weather App")
photo=ImageTk.PhotoImage(Image.open("homeicon.png"))
root.iconphoto(True, photo)
#root.configure(background=weather_colour)     #we'll be having to put this line inside the try loop after we've mentioned what weather_colour is

#this is called try-loop or trial loop
try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=42001&distance=5&API_KEY=1B919C74-7D79-4786-9712-9B5DB7F72D3F")
    
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

    if category == "Good":
        weather_color = "#00e400"
    elif category == "Moderate":
        weather_color = "#ffff00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff7e00"
    elif category == "Unhealthy":
        weather_color = "#ff0000"
    elif category == "Very Unhealthy":
        weather_color = "#8f3f97"
    elif category == "Hazardous":
        weather_color = "#7e0023"

    root.configure(background=weather_color)

    mylabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)  #20=font size
    mylabel.pack()    

except Exception as e:
    api = "Error..."

'''
mylabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background="green")  #20=font size
mylabel.pack()
'''

root.mainloop()