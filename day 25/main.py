# with open(file="day 25\weather_data.csv") as weather_data:
#   data = weather_data.readlines()
#   print(data)

# import csv

# with open(file="day 25\weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       row = int(row[1])
#       temperatures.append(row)
    

#   print(temperatures)

import pandas

# data = pandas.read_csv("day 25\weather_data.csv")
# temp_list =(data[data.temp == data["temp"].max()])
# print(temp_list)

data = pandas.read_csv("day 25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

my_dict = {
  "fur color": ["Gray", "Cinnamon", "Black"],
  "Count" : [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}
print(my_dict)
pf = pandas.DataFrame(my_dict)
pf.to_csv("squirrel_count.csv")