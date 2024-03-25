def lucky_customer_order_id(N):
    # Initialize the sequence with the first two numbers
    sequence = [1, 1]
    
    # Generate the sequence up to N terms
    while len(sequence) < N:
        next_number = sum(sequence[-2:])  # Calculate the next number as the sum of the last two numbers
        sequence.append(next_number)  # Add the next number to the sequence
    
    # Return the Nth number which is treated as the order ID
    return sequence[-1]  


# Input from the user
N = int(input("Enter a number: "))

# Get the order ID for the lucky customer
order_id = lucky_customer_order_id(N)

# Output the order ID
print("Order ID:", order_id)
