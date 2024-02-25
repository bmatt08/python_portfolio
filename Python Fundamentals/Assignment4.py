def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #Write your logic
    if not(food_type=="V" or food_type=="N"):
        bill_amount=0
    elif distance_in_kms<=0:
        bill_amount=-1
    elif quantity_ordered<1:
        bill_amount=-1
    else:
        if food_type=="N":
            bill_amount=150*quantity_ordered
        else:
            bill_amount=120*quantity_ordered

        delivery_charge=0
        if distance_in_kms>3 and distance_in_kms<=6:
            delivery_charge=(distance_in_kms-3)*3
        elif distance_in_kms>6:
            delivery_charge=(distance_in_kms-6)*6+9
        bill_amount+=delivery_charge
    return bill_amount

bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)