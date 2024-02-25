def solve(heads, legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if legs%2!=0 or heads>legs:
        print(error_msg)
    for chicken_count in range(heads+1):
        rabbit_count = heads - chicken_count
        if(4 * rabbit_count + 2 * chicken_count == legs):
            print(chicken_count,rabbit_count)
            break
    
    # populate the variables: chicken_count and rabbit_count
    # Use the below given print statements to display output
    #print(chicken_count,rabbit_count)
    #print(error_msg)

solve(10,40)