# import csv

# rows = []

# with open ("Day 25 - Pandas and CSVs\weather_data.csv", newline="") as csvfile:
#     reader = csv.reader(csvfile)
#     temperatures = []
#     for row in reader:
#         rows.append(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(rows)
# print(temperatures)

# import pandas as pd


# data = pd.read_csv("Day 25 - Pandas and CSVs\weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# ave_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# #Get Data in a row
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# monday_celsius = (monday.temp * 5/9)  + 32
# print(monday_celsius)



import pandas as pd

data = pd.read_csv(r"Day 25 - Pandas and CSVs\2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240314.csv")
color_data = data["Primary Fur Color"].value_counts()
df = pd.DataFrame(color_data)
df.to_csv(r"Day 25 - Pandas and CSVs\Squirrel_fur_count.csv")


