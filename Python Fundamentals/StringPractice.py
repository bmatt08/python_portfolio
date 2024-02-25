'''
validate email id
<first>@<second>.com
<first> should be only alphabets and numbers and should be min 3 chars
<second> should be only alphabet min 2 chars
valid ex: alex123@email.com
invalid ex: al-ex@email.com
        ex2: alex
        ex3: alex@emailcom

'''

def validate_email(email):
    if email.count("@")!=1:
        return False
    first=email[0:email.index("@")];
    if len(first)<3 or not first.isalnum():
        return False
    if email[-4:]!=".com":
        return False
    second=email[email.index("@")+1:email.index(".com")]
    if len(second)<2 or not second.isalpha():
        return False
    return True

print(validate_email("Chris@email.com"))


'''
Write A Program to find how many emails in a list are valid
'''
def count_valid_emails(email_list):
    count=0
    for email in email_list:
        if validate_email(email):
            count+=1
    
    return count


res=count_valid_emails(["Christian@email.com", "Alex-12@gmail.com", "Austin@email.com", "Lloyd@email.com", "Sid@gmail.com"])
print(res)
    