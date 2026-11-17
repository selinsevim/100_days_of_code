# with open(
#     "/Users/selinsevim/Documents/100_days_of_code/Day_25/weather_data.csv", mode="r"
# ) as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv

# with open(
#     "/Users/selinsevim/Documents/100_days_of_code/Day_25/weather_data.csv", mode="r"
# ) as weather_file:
#     data = csv.reader(weather_file)
#     data_list = list(data)
#     temperature = []
#     for row in data_list[1:]:
#         temperature.append(int(row[1]))

# print(temperature)

import pandas as pd

data = pd.read_csv(
    "/Users/selinsevim/Documents/100_days_of_code/Day_25/weather_data.csv"
)
temperature = []
temperature.append(data["temp"])
print(temperature)
