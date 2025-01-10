from flask import Flask, render_template, request 
  
# import json to load JSON data to a python dictionary 
import json 
  
# urllib.request to make a request to api 
import urllib.request 
  
  
app = Flask(__name__) 
  
# Route to handle both POST and GET requests
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city']          # Get the city name from the form if the request is POST     
    else: 
        # Default city is 'mumbai' if no city is provided
        city = 'mumbai'
  
    # API key for OpenWeatherMap 
    api_key = 'bfded00eb9ee818074bc2745de187c87'
  
    # source contain json data from api 
    source = urllib.request.urlopen(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}").read() 
  
    # converting JSON data to a Python dictionary 
    list_of_data = json.loads(source) 
  
    # data for variable list_of_data ( data to display on the webpage )
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": f"{ str(list_of_data['coord']['lon']) }° { 'E' if (list_of_data['coord']['lon']) >= 0 else 'W'},  { str(list_of_data['coord']['lat']) }° { 'N' if (list_of_data['coord']['lat']) >= 0 else 'S'}", 
        "temp": f"{ str(list_of_data['main']['temp']) } K ", 
        "pressure": f"{ str(list_of_data['main']['pressure'])}mbar ", 
        "humidity":f"{ str(list_of_data['main']['humidity']) }% ", 
        "cityname":str(list_of_data['name']),
        "temp_cel":f"{ str( round( (list_of_data['main']['temp']) - 273.15 , 2) ) } °C ",
    
    } 
    print(data) 
    return render_template('index.html', data = data) 
  
  
  
if __name__ == '__main__': 
    app.run(debug = True)
