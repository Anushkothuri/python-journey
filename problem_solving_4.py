#PROBLEM 1
#replace()
num="+49 (176) 123-4567"
print(num.replace("+","00").replace("(","").replace(")","").replace("-",""))
print()
#PROBLEM 2
#plus(+)
file="C:/Users/Anush/"
folder="reports"
full_file_path=file+folder
print(full_file_path)
print()
#PROBLEM 3
s="968-Maria, ( D@t@ Engineer ) ;; 27y  "
name=s.split("-")[1].split(",")[0].strip()
role=s.split("(")[1].split(")")[0].strip()
age=int(s.split(";;")[1].replace("y","").replace('"',"").strip())
role=role.replace("@","a").lower()
print("name: ",name.lower())
print("role: ",role)
print("age: ",age)