def validate_name(name):
    if name == "" or len(name) > 15:
        return False
    if not name.isalpha():
        return False
    return True

def validate_phone_no(phno):
    if len(phno)!=10 or not phno.isdigit():
        return False
    for i in phno:
        if phno[0]!=i:
            return True
    return False

def validate_email_id(email_id):
    if email_id.count("@")!=1 or email_id[-4:] != ".com":
        return False
    domain=email_id[email_id.index("@")+1:email_id.index(".com")]
    if not (domain == "gmail" or domain == "yahoo" or domain == "hotmail"):
        return False
    return True

def validate_all(name,phone_no,email_id):
    if not validate_name(name):
        print("Invalid Name")
    elif not validate_phone_no(phone_no):
        print("Invalid Phone Number")
    elif not validate_email_id(email_id):
        print("Invalid Email Id")
    else:
        print("All the details are valid")

validate_all("Tina","9994599998", "tina@yahoo.com")