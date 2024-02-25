def remove_duplicates(value):
    str1 = ""
    for char in value:
        if(not(char in str1)):
            str1+=char
    return str1

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
