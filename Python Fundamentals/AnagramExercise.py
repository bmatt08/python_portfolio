def check_anagram(data1,data2):
    str1=data1.lower()
    str2=data2.lower()
    if len(str1)!=len(str2):
        return False

    for i in range(len(data1)):
        if str1[i] not in str2 or str1[i]==str2[i] or str2[i] not in str1:
            return False
    return True

print(check_anagram("eat","tea"))