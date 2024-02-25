def sub(a,b):
    return a-b

sub(20,5)   #positional

def div(a,b):
    return a/b
x=25
y=5
print(div(b=y,a=x)) #keyword

def mul(a,b=10):    #default value
    return a*b

print(mul(5,5))
print(mul(5))

def add(a,*b):  #variable arguments
    sum=0
    for i in b:
        sum+=i
    return sum
print(add("Tad",10,20,30,40,50))