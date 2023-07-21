# with open("weather_data.csv") as names_file:
#     data = names_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for weather in data:
#         if weather[1] != "temp":
#             temperature.append(int(weather[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather_data.csv")
# temp = data["temp"]
# print(temp)
# dict_convert = data.to_dict()
# print(dict_convert.keys())
# print(dict_convert.values())

# max = temp.max()
# print(max)
# avg = sum(temp)/len(temp)
# print(avg)
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# fed = (monday.temp)*9/5+32
# print(fed)
