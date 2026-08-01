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
print()
#f-string
name="Anush"
age=20
Is_Student=True
print(f"my name is {name}, I am {age} year old and student status is {Is_Student}.")
#split()
stamp="2026-09-20 14:30"
print(stamp.split("-"))
# repetator *
print("Ha"*3)
print("-"*7) 
#indexing and slicing
text = "Python"
print(text[0])     #positive indexing
print(text[-6])    #negative indexing
print(text[0:4])   #positive slicing
print(text[-6:-2]) #negative slicing
print(text[0:4:2]) #step slicing
#strip()
text=" Anush".lstrip()
print(text)
text="Anush ".rstrip()
print(text)
text=" Anush ".strip()
print(text)
text="##Anush###".strip("#")
print(text)
text=" Engineering "
print(len(text))
print(len(text.strip()))
print(len(text)-len(text.strip()))
print(len(text)==len(text.strip()))