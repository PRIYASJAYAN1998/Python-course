def add(value1,value2):
    result= value1+value2
    return result

def mul(value1,value2):
    result=value1*value2
    return result

def sub(value1,value2):
    result=value1-value2
    return result

def div(value1,value2):
    result=value1/value2
    return result

operation=input("enter the operation")
a=int(input("enter the first value"))
b=int(input("enter the second value"))
if operation=="+":
    ans=add(a,b)
    print(ans)
elif operation=="*":
    ans=mul(a,b)
    print(ans)
elif operation=="-":
    ans=sub(a,b)
    print(ans)
elif operation=="/":
    ans=div(a,b)
    print(ans) 

else:
    print("invalid operation")
