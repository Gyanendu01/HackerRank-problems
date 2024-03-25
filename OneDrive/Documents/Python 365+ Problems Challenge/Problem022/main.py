n = input('Enter a number: ')

sum = 0
for i in n:
    sum = sum +int(i)

# Niven number is that number that is divisible by the sum of its digits
if int(n)%sum == 0:
    print('Yes')
else:
    print('No')