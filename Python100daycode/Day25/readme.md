# Working with CSV files and Analyzing Data with Pandas

Reading CSV (coma separated value) data - it is very common way to represent the tableaur data 

```py 
with open("Python100daycode/Day25/weather_data.csv",mode="r") as file:
    data=file.readlines()
    print(data)   # but this will be very painful, instead use csv library 

```

```py

import csv

with open("Python100daycode/Day25/weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures=[]
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)    ### this also not the best way 

```

## Pandas - Python data analysis library 
It is powerful data analysis library for the tabula data

pip3 install pandas
pandas documentation: <https://pandas.pydata.org/docs/>

pandas API reference: <https://pandas.pydata.org/docs/reference/index.html>

```py 
import pandas

data = pandas.read_csv("Python100daycode/Day25/weather_data.csv")
print(data)
print(data["temp"])

```

