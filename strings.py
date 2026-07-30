#STRINGS
#type()
name="Anush"
print(type(name))
print() #line gap
#str()
age=21
print("Age is: "+str(age)) #int converts to str
age=age+1
print(age)
print() #line gap
#len()
id="anush"
print(len(id))
if len(id)<8:
    print("Invalid")
print()
#count()
text=""" 
Python is easy to learn.
I love python.
Python is powerful!
"""
print(text.count("Python"))