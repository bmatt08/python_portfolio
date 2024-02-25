def check_perfect_number(number):
    sum_of_divisors=0
    if number==0:
        return False
    for i in range(1, number):
        if number % i == 0:
            sum_of_divisors+=i
    return number == sum_of_divisors

def check_perfectno_from_list(no_list):
    perfect_list=[]
    for i in no_list:
        if check_perfect_number(i):
            perfect_list.append(i)
    return perfect_list

#   print(check_perfect_number(28))
perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)