# by casting or dynamic typing we can change the datatype of the variable in the pyhton

# but like in c++ we can also specify the type of variable datatype if needed


age: int
name: str
height: float
is_human: bool

## data type in function also called type Hints
def police_check(age: int) -> bool:  ## this means age should be int and this function should return bool
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")







