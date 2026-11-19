import pandas as pd

data = pd.read_csv(
    "/Users/selinsevim/Documents/100_days_of_code/Day_25/nyc_squirrel_challenge/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

# find the number of black
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_count)
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_count)

dataframe = {
    "fur_color": ["Black", "Gray", "Cinnamon"],
    "count": [black_count, grey_count, cinnamon_count],
}

squirrel_data = pd.DataFrame(data=dataframe)
print(squirrel_data)

# Shortcut
# new_data = data["Primary Fur Color"].value_counts()
# new_data.to_csv("new.csv")
