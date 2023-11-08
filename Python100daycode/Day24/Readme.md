# File system management using Python

<https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files>

Reading a text file

```py

file = open("Python100daycode/Day24/read_write/my_file.txt")
contents = file.read()
print(contents)
file.close() # manually closing the file 

```

Using with to open file, this open file temporarily

```py

with open("Python100daycode/Day24/read_write/my_file.txt") as file:
    contents = file.read()
    print(contents)

```

open and write in file

```py
#open and write in file

with open("Python100daycode/Day24/read_write/my_file.txt",mode="w") as file:
    file.write("Hello world!")
```

open and append in file

```py
#open and append in file

with open("Python100daycode/Day24/read_write/my_file.txt",mode="a") as file:
    file.write("\nMy name is Prabh.")
```

create a new file

```py
#create a new file
# in write mode if that file don't exist it will create a new file from scratch
with open("Python100daycode/Day24/read_write/new_file.txt",mode="w") as file:
    file.write("Hello world!")
```

## Relative and absolute file paths
Absolute file paths starts from the root
