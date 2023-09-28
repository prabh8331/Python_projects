#When return hits in function the execution of function will stop 
#and it will return value and nothing after the return will get executed  

def format_name(f_name,l_name):
    if f_name == "" or l_name=="":
        return "You didn't provided valid inputs"
    name=f_name+" "+l_name
    return(name.title())

name = format_name("pRabH","siNgh") # 'Prabh Singh'
print(name)

def is_leap(year):
  """ Return True if Leap year, else Returns False"""
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
  
is_leap()