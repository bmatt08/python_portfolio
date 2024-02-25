# my_list=[1234,1254,5432,6554,7865, 2345]
# print(len(my_list))
# my_list[2]=1111
# my_list[3]=4567
# print("printing the list using range()")
# for i in range(0,len(my_list)):
#       print(my_list[i])
# print("printing the list using for in list syntax")
# for x in my_list:
#       print(x)



name_list=["Chris", "John", "Alec", "Austin", "Trevor", "Lloyd"]
name_list2=["Osa", "Greg", "Daniel"]

name_list.pop(2)
print(name_list)
new_list=name_list+name_list2
new_list.append("Tad")
new_list.insert(1, "Osa")

print(name_list)

new_list.reverse()
print(new_list)
print(new_list.count("Osa"))
print(new_list.count("Trevor"))
print(new_list.count("Blane"))
while(new_list.count("Osa")>0):
        new_list.remove("Osa")

print(new_list)