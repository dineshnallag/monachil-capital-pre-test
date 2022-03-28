import rainy
import util

rainy = rainy.RAINY("data.csv")
rain_data = rainy.get_raindata()
cityname = rainy.get_cityname()
city_data = rainy.get_data(cityname)
city_latitude, city_longitude = rainy.get_coordinates(city_data)
dates = util.generate_dates(rain_data, city_latitude, city_longitude)

print("Number of rainy 5-days: "+str(len(dates)))