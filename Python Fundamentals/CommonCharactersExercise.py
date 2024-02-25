def find_common_characters(msg1,msg2):
    shared_characters=""
    for char in msg1:
        if char.count(" ")==1:
            continue
        if char in msg2 and char not in shared_characters:
            shared_characters += char
    if shared_characters == "":
        return -1
    return shared_characters

msg1="I like Python"
msg2="I prefer Java"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)