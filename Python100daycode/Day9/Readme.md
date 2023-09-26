### Dictionary in Python 

```py
##Python Dictionaries
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
    
#Create an empty dictionary.
new_dictionary = {}

new_dictionary = {"Bob",[1,2,3]}

#Wipe an existing dictionary
new_dictionary = {}
print(new_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
#print(programming_dictionary)

#Loop through a dictionary
 for key in programming_dictionary:
   print(key)
   print(programming_dictionary[key])

```

#### Write a program that converts students scores to grades

```py

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.
for key in student_scores:
    score=student_scores[key]
    if score >=91:
        grade="Outstanding"
    elif score >=81:
        grade="Exceeds Expectations"
    elif score>=71:
        grade="Acceptable"
    else:
        grade="Fail"
    student_grades[key]=grade
    

print(student_grades)

```

#### Nesting Lists and Dictionaries 

```py

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

#only down side of mixing datatype in dictionary is you should know what datatype is that
```

#### Define function to add new values is nested 

```py 
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

#TODO: Write the function that will allow new countries to be added to the travel_log.

def add_new_country(country, visits,cities):
    travel_log.append({"country": country,"visits": visits,"cities": cities})

## or

def add_new_country(country, visits, cities):
    country_visit={}
    country_visit["country"]=country
    country_visit["visits"]=visits
    country_visit["cities"]=cities
    travel_log.append(country_visit)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

```

