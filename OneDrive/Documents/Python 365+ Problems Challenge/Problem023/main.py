n = input('Enter a number: ')

sum = 0
product = 1

for i in n:
    sum = sum +int(i)
    product = product*int(i)

result = sum + product
# special two digit number is a number such that when the sum of its digits is added to the product of its digits, the result should be equal to the original two-digit number.
if int(n) == result:
    print('Yes')
else:
    print('No')