n = int(input("Enter a number: "))
reversedNum = []
if n > 0:
    while n>=0:
        reversedNum.append(n%10)
        n = n//10

reversedNum.sort(reverse=True)
for i in reversedNum:
    print(i,end='')
