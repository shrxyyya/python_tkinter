#build a basic weather app

#firstly we go to airnow.gov (just a sample website from where we taking in the data for the project)
'''
Then we go to the documents tab to access the documentation and to be able to connect to the API. For tht we first login to that site.
Then alongside the documentation, we find a query tool which is the one we'll be using coz we needed to create a query.
In the query tool, we fill in the zipcode and the radius within which we want the data to be taken, and then they ask us in which format
we want the file, so here... CHOOSE JSON. Json is the type which we usually wld want to use to connect to APIs.
'''

from tkinter import *
from PIL import ImageTk, Image
#now, we want to connect to a third party API and bring back data from it... one of the ways of doing so is by using 'requests' ==> Requests is an HTTP library in python
import requests
#now importing 'requests' brings back the data as 'json' file but we need to be able to decode it... so we import json
#The data in JSON is represented as quoted-strings consisting of key-value mapping enclosed between curly brackets {}.
import json
#json.loads() method can be used to resolve a valid JSON string into its components and convert it into a Python Dictionary.

root=Tk()
root.geometry("400x40")
root.title("Weather App")
photo=ImageTk.PhotoImage(Image.open("homeicon.png"))
root.iconphoto(True, photo)
root.configure(background='green')  #we do this to cover the background green spaces after we add bg colour as green in the label section

#https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=1B919C74-7D79-4786-9712-9B5DB7F72D3F

#we are doing a bit of error-handling now
try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=1B919C74-7D79-4786-9712-9B5DB7F72D3F")
    
    #we want to pass wtv data we are getting through api_request into the api variable
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."
#so what this does is we wanna try that main json.loads wala code. And if it doesn't work, we want an error to be thrown.

#mylabel = Label(root, text = api[0]['Category']['Name'])
mylabel = Label(root, text = city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background="green")  #20=font size
mylabel.pack()

root.mainloop()

'''
when we go to the docs of the website we're referring to here, and when we head to the query tool, the query tool gives us that url that we've pasted
and it also has a place wher we could run the url thing to see the output.
On analysing the output, we see that it is actually a list consisting of 3 dictionaries, the first one tells abt the ozone info, the secong abt PM 2.5 and
the third tells abt PM 10. So here for now er're only concerned with the ozone part ==> since, its a list consisting of dict and ozone is first dict,
so it'll have the index value=0. So we use this index value to call the ozone dict as we are only concerned with ozone related info here.
Then after accessing the ozone realted info, we wanted to access the Reporting Area or the area of which we want to know the AQI of. --> again using indexing (with help of keys)
pr if we want to see the AQI, we can look it up by entering it as the key.
'''