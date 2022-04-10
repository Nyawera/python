from unicodedata import name
age= 40
name ="kobby"
print(name.format(age))
data = "hello my name is {}and age is{} "
print(data.format(name,age))

name = "Arthur"
age= 45
Nationality= "sudan"

description = "My name is {1}and I am {2} years old"
print(description.format(Nationality,name,age))