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
print(type(data))
print(type(data["temp"]))
temperature = data["temp"]
average_temp = temperature.mean()
print(average_temp)
max_value = temperature.max()
print(max_value)

# you treat like list
print(data["condition"])
# you treat like object
print(data.condition)

# Find the row that has Monday as a day
print(data[data["day"] == "Monday"])

# Find the row with the highes temperature
print(data[data["temp"] == data["temp"].max()])

# You can go one step further to get specific column data of the specific row
monday = data[data["day"] == "Monday"]
print(monday["temp"])
