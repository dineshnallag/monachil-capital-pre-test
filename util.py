DISTANCE_THRESHOLD=0.05
RAIN_THRESHOLD=8.0

def calculate_coordinate_diff(val1, val2):
  return abs(float(val1) - float(val2))

def generate_dates(rain_data, city_latitude, city_longitude):
  dates = list()
  for th, lat, lon, rain in rain_data:
    th = th[:10]
    latitude_difference = calculate_coordinate_diff(lat, city_latitude)
    longitude_difference = calculate_coordinate_diff(lon, city_longitude)
    if rain != "NaN":
      if float(rain) >= RAIN_THRESHOLD:
        if latitude_difference < DISTANCE_THRESHOLD:
          if longitude_difference < DISTANCE_THRESHOLD:
            dates.append((th,rain))
  return dates