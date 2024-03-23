n = int(input("Enter a number: "))
sum = 0
if n > 0:
    while n>0:
        if n%10 in [2,3,5,7]:
            sum = sum+(n%10) 
        n = n//10

print("\nSum Of Prime digitss is: {}".format(sum))
