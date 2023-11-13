# List and Dictionary Comprehensions

## List comprehension

Old method using For Loop

```py
# if we want a new list with each number increased then:
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

```

Using List Comprehension: syntax `new_list = [new_item for item in list]`

```py
numbers = [1, 2, 3]

new_list = [n+1 for n in numbers]
```

Python Sequence : list, range , string , tuple has a sequence because they have a perticular order
Few Examples: 

```py

numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
new_numbers #[2, 3, 4]
name = "Angela"
new_list = [letter for letter in name]
new_list #['A', 'n', 'g', 'e', 'l', 'a']
list_range = [n*2 for n in range(1,5)]
list_range # [2, 4, 6, 8]

```

### Conditional List comprehension
syntax: new_list = [new_item for item in list if test]

```py 

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
names #['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name)<=4]
short_names #['Alex', 'Beth', 'Dave']

long_names = [name.upper() for name in names if len(name) > 4] # ['CAROLINE', 'ELEANOR', 'FREDDIE']

```

Problems

```py
#Problems

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# square the numbers
squared_numbers = [number*number for number in numbers]
print(squared_numbers)

# filter the even numbers
string_numbers = "1 2 3 12 34 36 4 52 345 38 6".split(' ')

numbers = [int(num) for num in string_numbers]

even_numbers = [num for num in numbers if num%2 == 0]
print(even_numbers)
```

## Dictionary Comprehension

Syntax: 
new_dict = {new_key: new_value for item in list} <br>
new_dict = {new_key:new_value for (key,value) in dict.items()}
new_dict = {new_key:new_value for (key,value) in dict.items() if test}

Passed students:

```py

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {key: random.randint(1,100) for key in names}
# {'Alex': 67, 'Beth': 79, 'Caroline': 42, 'Dave': 23, 'Eleanor': 76, 'Freddie': 12}

passed_students = {student:marks for (student, marks) in students_scores.items() if marks> 33}
# {'Alex': 67, 'Beth': 79, 'Caroline': 42, 'Eleanor': 76}

```

Count of each word in a sentence:

```py

sentence = "What is the Airspeed Velocity of an Unladen Svallow?"

words = sentence.split(" ")

char_count = {print(word) for word in words}

char_count = {word: len(word) for word in words}

print(char_count)

```

Temperature Celsius to Fahrenheit

```py

#value = eval(input()) # input --> {'Monday':  12, 'Tuesday':  14, 'Wednesday':  15, 'Thursday':  14, 'Friday':  13, 'Saturday': 16, 'Sunday': 24}

# temp_c * 9/5 + 32 = temp_f

temp_c = {
    'Monday':  12,
    'Tuesday':  14,
    'Wednesday':  15,
    'Thursday':  14,
    'Friday':  13,
    'Saturday': 16,
    'Sunday': 24
}

temp_f = {print(day, temp) for (day, temp) in temp_c.items()}

temp_f = {day:temp* 9/5 + 32 for (day, temp) in temp_c.items()}
print(temp_f)

```

### iterate over a Pandas DataFrame

```py
student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}

# loop through the dictionary 

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)


import pandas

student_df = pandas.DataFrame(student_dict)
# print(student_df)

## this method is iteration through the columns, not that useful
# for (key, value) in student_df.items():
#     print(key)
#     print(value)
    

# pandas inbuilt method to iterate through the rows 

for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)
```
