n = int(input("Enter a number: "))
sum = 0
if n > 0:
    while n>0:
        digit = n%10
        if digit%3==0:
            sum = sum+(n%10) 
        n = n//10

print("\nSum Digits is: {}".format(sum))
