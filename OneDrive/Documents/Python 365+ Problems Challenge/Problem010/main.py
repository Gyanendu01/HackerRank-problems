n = int(input("Enter a number: "))
sum = 0
if n > 0:
    while n>0:
        if n%2!=0:
            sum = sum+(n%10) 
        n = n//10

print("\nSum Digits divisible by 2 is: {}".format(sum))
