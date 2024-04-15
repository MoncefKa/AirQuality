import requests

g=requests.get("http://dataservice.accuweather.com/locations/v1/adminareas/countryCode?apikey=BZEDaGN5Fb8kIg2A9o8jZQjS6QONXzlA")

print(g.json())