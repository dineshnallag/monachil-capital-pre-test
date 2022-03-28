import csv
import this
import requests

class RAINY:
  def __init__(self, file):
    this.file = file
  
  def get_raindata(self):
    csv_file = open(this.file)
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    rain_data = list()
    for row in csv_reader:
      line_count += 1
      if line_count <= 2:
        print(f'Column names are {", ".join(row)}')
        continue
      elif line_count >= 10e10:
        break
      rain_data.append(row)
    csv_file.close()
    return rain_data
  
  def get_cityname(self):
    return str(input("Enter city name:[San Jose]: ") or "San Jose")
  
  def get_data(self, city):
    return requests.get("https://nominatim.openstreetmap.org/search.php?city="+city+"&format=jsonv2&namedetails=0&addressdetails=0&limit=1").json()
  
  def get_coordinates(self, city_data):
    return city_data[0]['lat'], city_data[0]['lon']