def check_double(number):
    num = str(number)
    num_double=str(number*2)
    same = False
    for i in range(0, len(num)):
        if(num[i] != num_double[i] and num_double[i] in num):
            same = True
        else:
            same = False
    return same

print(check_double(125874))