def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write Logic Here

    rate_adult = 375*no_of_adults
    rate_child = 375/3*no_of_children
    total=(rate_adult+rate_child)
    total=total+total*7/100
    discount=total*.10
    total_ticket_cost=total-discount
    return total_ticket_cost

#Provide different values for no_of_adults, no_of_children and test program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:", total_ticket_cost)