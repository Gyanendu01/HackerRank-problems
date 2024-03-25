n = int(input('Enter the bill amount: '))

sum = 0
while n>0:
    digit = n%10
    if digit in [2,3,5,7]:
        sum += digit
    n = n//10

print(sum)