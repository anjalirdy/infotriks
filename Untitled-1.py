import pip._vendor.requests


api_key='d1a5dbe6789fd1ad7cc9c5dec3eb810c' 

user_input=input("Enter city:")
user_input=input("Enter fav list of city")
user_input=input("Enter auto refresh ")
weather_data =pip._vendor.requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

print(weather_data.status_code)
print(weather_data.json())
if weather_data.json()['cod']=='404':
   print("no city found")
else:
    weather= weather_data.json()['weather'][0]['main']
    temp=round(weather_data.json()['main']['temp'])
    print(weather,temp)
    print(f"The weather  in {user_input} is:{weather}")
    print(f"The temperature is {user_input} is:{temp}F")