def calculate_sum(a,b,name): #function header
    result=a+b+b        #function body
    greet(name)
    return result

def greet(name):
    if(name=="Lloyd"):
        return
    print("Hello",name)

def get_PI():
    return 3.14192


print("Program starts here")
print(calculate_sum(5,6,"Lloyd"))
print(calculate_sum(15,6,"Kevin"))
print("Program ends here")