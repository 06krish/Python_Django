print("hello world")
a = [10,20,30,40,50]
b = [10,20,30,40,50]
print(a==b)
# it is stored in different memory location so it will return false
print(a is b)

marks = int(input("enter your marks: "))
if marks>=60:
    print("pass")
else:
    print("fail")
# usage of loop 
students = ["Alice","bob","charlie","david","eve"]
for student in students:
    print(student)
for i in range(len(students)):
    print(students[i])
# in the range function we can specify the start, stop and step values
for i in range(1,11,2):
    print(i)

for i in range(1,20):
    if(i%2 == 0):
        continue
    else:
        print(i)
print("\n")
for i in range(1,20):
    if(i==15):
        break
    else:
        print(i)

# indexing in string
name = "Krish"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name.upper())
new_name = name.replace("Krish","Krish Raj")
print(new_name)
# dictionery
student ={
    "name":"Krish",
    "age":20,
    "Department":"CSE",
}
print(student["name"])
print(student.get("age"))
print(student.keys())
print(student.values())
# it gives the key value pair in the form of tuple
print(student.items())

def add_number(a,b):
    return a+b
print(add_number(10,20))
# simple calculator using function
def calculator(a,b,opr):
    if(opr == "+"):
        return a+b
    if(opr == "-"):
        return a-b
    if(opr == "*"):
        return a*b
    if(opr == "/"):
        return a/b
    if(opr == "%"):
        return a%b
    if(opr == "**"):
        return a**b
    if(opr == "//"):
        return a//b
    else:
        print("invalid operator")

print(calculator(10,20,"+"))

# modules in python 
import math
