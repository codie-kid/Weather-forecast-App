#Weather forecast

import tkinter,requests
from tkinter import BOTH , IntVar

#define window

root = tkinter.Tk()
root.title("Weather forcast")
root.iconbitmap('weather.ico')
root.geometry('400x400')
root.resizable(0,0)


#Define colors
sky_color = '#76c3ef'
grass_color = '#aad207'
output_color = '#dcf0fb'
input_color = '#ecf2ae'
large_font = ('Simsun' , 14)
small_font = ('Simsun', 10)

#Define function

def search():
    """Use open weather API to look up current weather condition given a city ,city , country"""
    global response
    #Get API response
    #URL and my api key ......USE YOUR OWN API KEY!
    url = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = '9171dc481b85db17e030210c545927c7'

    #Search by the appropriate query , either city or zip
    if search_method.get() == 1:
        querystring = {"q" : city_entry.get() , "appid" :api_key}
    elif search_method.get() == 2:
        querystring = {"zip" : city_entry.get() , "appid" : api_key}
    
    #call API
    response = requests.request("GET" , url , params = querystring)
    response = response.json()
    
    #Example response return
    #{'coord': {'lon': 85.33, 'lat': 27.67}, 'weather': 
    # [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}],
    # 'base': 'stations', 'main': {'temp': 291.15, 'feels_like': 289.42, 'temp_min': 291.15,
    # 'temp_max': 291.15, 'pressure': 1023, 'humidity': 55}, 'visibility': 8000,
    # 'wind': {'speed': 2.1, 'deg': 250}, 'clouds': {'all': 20}, 'dt': 1604838534,
    # 'sys': {'type': 1, 'id': 9201, 'country': 'NP', 'sunrise': 1604795673, 'sunset': 1604835022},
    # 'timezone': 20700, 'id': 1282931, 'name': 'Patan', 'cod': 200}
    get_weather()
    





def get_weather():
    """Grab information from API response and update our weather labels"""
    #gather the data to be used from the API
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_weather = response['weather'][0]['main']
    description = response['weather'][0]['description']
    temp = str(response['main']['temp'])
    feels_like = str(response['main']['feels_like'])
    temp_min = str(response['main']['temp_min'])
    temp_max = str(response['main']['temp_max'])
    humidity = str(response['main']['humidity'])

    #update output labels

    city_info_label.config(text = city_name + "(" + city_lat + "," + city_lon + ")", font = large_font ,bg = output_color ) 
    weather_label.config(text = "weather :" + main_weather + "," +description , font = small_font , bg = output_color)
    temp_label.config(text = 'Temperature:'  +temp + "F", font = small_font ,bg = output_color)
    feels_label.config(text ='feel_like:' + feels_like +"F" , font = small_font ,bg = output_color)
    temp_min_label.config(text ="Min Temperature: " + temp_min + "F", font = small_font , bg = output_color)
    temp_max_label.config(text = "Max Temperature:" +temp_max+"F" , font =small_font , bg = output_color)
    humidity_label.config(text = "Humidity:" + humidity , font = small_font ,bg = output_color)



    







#Define layout

#create frame

sky_frame = tkinter.Frame(root , bg = sky_color , height = 250)
grass_frame = tkinter.Frame(root , bg = grass_color )
sky_frame.pack(fill = BOTH , expand = True)
grass_frame.pack(fill = BOTH , expand = True)

output_frame = tkinter.LabelFrame(sky_frame , bg = output_color , width = 325 , height = 225)
input_frame = tkinter.LabelFrame(grass_frame , bg = input_color , width = 325)
output_frame.pack(pady = 30)
output_frame.pack_propagate(0)
input_frame.pack(pady = 15)

#Output frame layout
city_info_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
weather_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
temp_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
feels_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
temp_min_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
temp_max_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
humidity_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')
photo_label = tkinter.Label(output_frame, bg = output_color, text = 'Testing')


city_info_label.pack(pady = 8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack(pady = 8)

#Input frame Layout
#create input frame button and entry

city_entry = tkinter.Entry(input_frame , width = 20 , font = large_font)
submit_button = tkinter.Button(input_frame , text = 'Submit' ,font = large_font ,bg = input_color , command = search)


search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame ,text ='Search by city name' , variable = search_method  , value = 1 , font = small_font , bg = input_color)
search_zip = tkinter.Radiobutton(input_frame ,text = "Search by zipcode" , variable = search_method , value = 2 , font = small_font , bg = input_color)

city_entry.grid(row = 0 , column = 0 , padx = 10 , pady = (10,0))
submit_button.grid(row = 0 , column = 1 , padx = 10 ,pady = (10,0))
search_city.grid(row = 1 , column = 0 , pady = 2)
search_zip.grid(row = 1 , column = 1 , pady = 2 , padx = 5)






root.mainloop()