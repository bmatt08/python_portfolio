def display(num):
    message=""
    #Write logic here
    if(num%3 == 0 and num%5 == 0):
        message="Zoom"
    elif(num%3 == 0):
        message="Zip"
    elif(num%5 == 0):
        message="Zap"
    else:
        message="Invalid"
    return message

#Provide different values for num
message=display(4)
print(message)