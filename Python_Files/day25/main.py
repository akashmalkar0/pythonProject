import pandas
data = pandas.read_csv("us_city.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
dict = {
    "colour": ["Gray", "Black", "Cinnamon"],
    "count": [gray_count, black_count, red_count]
}
df = pandas.DataFrame(dict)
df.to_csv("color")
