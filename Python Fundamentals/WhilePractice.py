'''
Write A Program to calculate sum of first n numbers
'''

# def calculate_sum(num):
#   i=1
#   sum=0
#   while(i<=num):
#       sum+=i  #1 3 6 10 15
#       i+=1    #2 3 4 5 6
#   return sum

#print(calculate_sum(5))
def calculate_sum(num):
    sum=0
    for i in range(1, num+1):
        sum+=i #1 3 6 10 15
    return sum
print(calculate_sum(10))


'''
Write A Program to reverse a number
input 12345
output 54321

input 12
output 21
'''

def reverse(num):
    result=0
    while(num>0):
        rem=num%10                  #7    6    5    4
        result=result*10+rem%10     #7    76   765  7654
        num=num//10                 #456  45   4    0
    return result

print(reverse(4567))

'''
Write A Program to find factorial of a number

3!--> 3*2*1=6
4!--> 4*3*2*1=24
5!--> 5*4*3*2*1=120
'''
def factorial(num):
    fact=1
    for i in range(1,num):
        fact*=i   #1    2   6   24  120
    return fact
print(factorial(5))
