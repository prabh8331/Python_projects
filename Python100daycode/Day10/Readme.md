#### Functions with Outputs 

Syntax:  
```py
def my_function():
    result=3*2
    return result 

output = my_funciton()  #result will be 6 
```

Example: 
```py
# Functions with outputs

def format_name(f_name,l_name):
    # fn1=""
    # ln1=""
    # fn1+=f_name[0].upper()
    # ln1+=l_name[0].upper()
    # for i in range(1,len(f_name)):
    #     fn1+=f_name[i].lower()        
    # for i in range(1,len(l_name)):
    #     ln1+=l_name[i].lower()
    # return(fn1+" "+ln1)
    name=f_name+" "+l_name
    name.title()

name = format_name("pRabH","siNgh") # 'Prabh Singh'
print(name)

```

Function with multiple return:
```py
#When return hits in function the execution of function will stop 
#and it will return value and nothing after the return will get executed  

def format_name(f_name,l_name):
    if f_name == "" or l_name=="":
        return "You didn't provided valid inputs"
    name=f_name+" "+l_name
    return(name.title())

name = format_name("pRabH","siNgh") # 'Prabh Singh'
print(name)

```


#### find no. of day in the give year and month 

```py
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return(True)
      else:
        return False
    else:
      return(True)
  else:
    return(False)

def days_in_month(year,month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True and month==2:
        return( month_days[month-1]+1)
    return(month_days[month-1])
    
  
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

```

#### Docstrings 
Docstring is a way to maintain documentation of function or other block of code

can also use it as a multiline comments

```py
def is_leap(year):
  """ Return True if Leap year, else False"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return(True)
      else:
        return False
    else:
      return(True)
  else:
    return(False)

```