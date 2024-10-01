# import csvfile
# import csv
# import pandas as pd

# # # opening a file using with open method
# # with open('weather_data.csv', 'r') as file:
# #     output = file.readline()

# # using csv package
# # with open('weather_data.csv', 'r') as file:
# #     output = csv.reader(file)
# #     for i in output:
# #         print(i[1])

# # # using a csvfile package
# # output = csvfile.load('weather_data.csv')
# # for i in output:
# #     print(i['temp'])
# # #print(output)

# #using pandas library
# output = pd.read_csv('weather_data.csv')
# #print(type(output))
# # print(type(output["temp"]))
# # print(output['temp'].max())
# # print(output['temp'].min())
# # print(output['temp'].mean())
# # print(output.condition)
# print(output[output.temp == output.temp.max()])

import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
data_gray = len(data[data['Primary Fur Color'] == "Gray"])
data_cinnamon = len(data[data['Primary Fur Color'] == "Cinnamon"])
data_black = len(data[data['Primary Fur Color'] == "Black"])
print(data_gray)
print(data_cinnamon)
print(data_black)
data_dict = {
    "fur_color": ["Gray", "Cinnamon", "Black"],
    "count" : [data_gray, data_cinnamon, data_black]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")