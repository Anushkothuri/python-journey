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
print(text.count("Python")) #count is case-senstive
print()
#replace()
price="1234,56"
print(price.replace(",", "."))
print()
#plus(+)
fir_name="Anush"
sec_name="Kothuri"
full_name=fir_name+" "+sec_name
print(full_name)