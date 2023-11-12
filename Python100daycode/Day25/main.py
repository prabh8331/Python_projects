# with open("Python100daycode/Day25/weather_data.csv",mode="r") as file:
#     data=file.readlines()
#     print(data)

# import csv

# with open("Python100daycode/Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures=[]
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Pandas

import pandas

# data = pandas.read_csv("Python100daycode/Day25/weather_data.csv")
# print(data)
# print(data["temp"])


# #Pandas provides two types of classes for handling data:

# # 1. Series: a one-dimensional labeled array holding data of any type such as integers, strings, Python objects etc.
# print(type(data["temp"]))   #<class 'pandas.core.series.Series'>  Series is like a list


# #2. DataFrame: a two-dimensional data structure that holds data like a two-dimension array or a table with rows and columns
# print(type(data))    #<class 'pandas.core.frame.DataFrame'>


# data_dict=data.to_dict()
# print(data_dict)


# data_list=data["temp"].to_list()
# print(data_list)

# print(sum(data["temp"]))

# print(len(data["temp"]))
# average = sum(data["temp"])/len(data["temp"])

# print(average)

# print(data["temp"].mean())

# print(data["temp"].max())


# # Get Data in Columns 
# print(data["condition"])
# print(data.temp)

# # get data in row
# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# monday.condition

# print((monday.temp * (9/5))+32)



# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Prabh"],
#     "scores": [76,56,75]
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("Python100daycode/Day25/new_data.csv")



data = pandas.read_csv("Python100daycode/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data["Primary Fur Color"].count())

print(data[data["Primary Fur Color"]=="Gray"]["Primary Fur Color"].count())
print(data[data["Primary Fur Color"]=="Cinnamon"]["Primary Fur Color"].count())
print(data[data["Primary Fur Color"]=="Black"]["Primary Fur Color"].count())

data_dict = {"Fur Color": ["grey","red","Black"],
 "Count": [data[data["Primary Fur Color"]=="Gray"]["Primary Fur Color"].count(),
           data[data["Primary Fur Color"]=="Cinnamon"]["Primary Fur Color"].count(),
           data[data["Primary Fur Color"]=="Black"]["Primary Fur Color"].count()]}

final_data = pandas.DataFrame(data_dict)

print(final_data)