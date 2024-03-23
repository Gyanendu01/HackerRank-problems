n = int(input("Enter a number: "))
numOfDigits = 0
if n > 0:
    while n>0:
        numOfDigits += 1
        n = n//10

print("\nNumber Digits is: {}".format(numOfDigits))
