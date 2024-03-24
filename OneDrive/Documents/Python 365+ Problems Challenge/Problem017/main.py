n = int(input("Enter a number: "))
num = n
reversedNum = ''
if n>0:
    while n!=0:
        reversedNum = reversedNum + str(n%10)
        n = n//10
reversedNum = int(reversedNum)
if reversedNum == num:
    print('Yes')
else:
    print('No')