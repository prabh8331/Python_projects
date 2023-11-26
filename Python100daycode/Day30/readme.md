# Error and Exception handling


```py

##### The try catch except finally pattern
####try: Something that might cause an exception
####except: Do this if there was an exception
####else: Do this iof there were no exceptions
####finally: Do this no matter what happens


try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")


# Raising your own exceptions

#BMI Example

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)





```