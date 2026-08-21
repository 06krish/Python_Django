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