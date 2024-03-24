n = int(input("Enter a number: "))
result = 'No'
if n > 0:
    while n>0:
        digit = n%10
        if digit == 0:
            result = 'Yes'
            break
        n = n//10
print(result)

