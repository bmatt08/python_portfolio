def change_val(num):
    num+=5

my_num=10
change_val(my_num)      #pass by value
print(my_num)

def change_list(num_list):
    num_list+=[5]

my_list=[10]
change_list(my_list)     #pass by reference
print(my_list)