x = int(input('Enter a number: '))
y = int(input('Enter another number: '))

sum = 0
for i in range(x,y+1):
    if i%2==0:
        sum = sum + i

print(sum)