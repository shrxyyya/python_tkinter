from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root=Tk()
root.title("Weather App")
root.geometry("800x400")
photo=ImageTk.PhotoImage(Image.open("homeicon.png"))
root.iconphoto(True, photo)

#Create Zipcode Lookup function
def ziplookup():
    #zip.get()
    #ziplabel = Label(root, text = zip.get())
    #ziplabel.grid(row = 1, column = 0, columnspan = 2)
    
    #now we want everything to happen after we click the button... so we put everything inside the button func definition

    try:
        #we need to change our API call-- we concatenate it with the zipcode
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=1B919C74-7D79-4786-9712-9B5DB7F72D3F")
        
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
        mylabel.grid(row=1, column=0, columnspan=2)    

    except Exception as e:
        api = "Error..."




zip = Entry(root)
zip.grid(row = 0, column = 0, stick=W+E+N+S)

zipbutton = Button(root, text = "Lookup Zipcode", command = ziplookup)
zipbutton.grid(row = 0, column = 1, stick=W+E+N+S)

root.mainloop()