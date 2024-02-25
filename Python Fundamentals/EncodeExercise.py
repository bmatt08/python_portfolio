def encode(message):
    count = 1
    new_message=""

    for i in range(0, len(message)-1):
        if(message[i]==message[i+1]):
            count += 1
        else:
            new_message+=(str(count)+message[i])
            count = 1
    new_message+=str(count)+message
    return new_message

encoded_message=encode("ABBBBCCCCCCCAB")
print(encoded_message)