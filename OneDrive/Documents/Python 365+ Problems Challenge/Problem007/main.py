n = int(input("Enter a number: "))
print("\nExtracted Digits are: ")
if n > 0:
    while n>0:
        print(n%10,end='')
        n = n//10
