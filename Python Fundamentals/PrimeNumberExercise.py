def check_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def rotations(num):
    # Should return the list of different combinations of digits of the given number
    # Rotation should be done clockwise
    rotated_list=[]
    for i in range(0,len(str(num))):
        rotated_list.append(int(str(num)[i:]+str(num)[:i]))
    
    return rotated_list

def get_circular_prime_count(limit):
    #Should return the count of circular prime numbers below the given limit
    circular_prime_list=[]
    for i in range(2,limit):
        circular_prime = True
        for n in rotations(i):
            if not check_prime(n):
                circular_prime=False
        if circular_prime:
            circular_prime_list.append(n)
    return len(circular_prime_list)

print(get_circular_prime_count(1000))