n = int(input("Enter a number: "))
num = n
d = int(input("Enter a number to calculate the occurrence of: "))
numOfOccurrences = 0
while n>0:
    if n%10 == d:
        numOfOccurrences += 1
    n = n//10

print("\nNumber of Occurrences of {} in {} is: {}".format(d,num,numOfOccurrences))
