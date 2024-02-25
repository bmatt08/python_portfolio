def find_max(num1,num2):
    max_num=-1

    num_list=[]
    if num1>=num2:
        return -1
    for num in range(num1,num2+1):
        if num>=10 and num<=99 and num%5==0:
            sum_of_digits=num%10+num//10
            if sum_of_digits%3==0:
                num_list.append(num)
    if len(num_list)==0:
        return -1

    max_num=max(num_list)

    return max_num

max_num=find_max(10,15)
print(max_num)