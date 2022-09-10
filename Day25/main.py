
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     # print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "Temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["Temp"].to_list()
# print(data_list)
#
# print(data["Temp"].max())
#
# print(data[data.Temp == data["Temp"].max()])
#
# monday = data[data.Day == "Monday"]
# print(monday.Condition)
# temp = int(monday.Temp)
# print(temp * 9/5 +32)

import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")

grey_color_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])


# print(grey_color_count)
# print(cinnamon_color_count)
# print(black_color_count)

# Creating a dataframe
data_dict = {
    "Fur color": ["grey", "cinnamon", "black"],
    "count": [grey_color_count, cinnamon_color_count, black_color_count]
}

# print(data_dict)

df = pd.DataFrame(data_dict)

df.to_csv("squirrel_count.csv")