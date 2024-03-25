def checkBirthday(month,date):
    if month.lower() == 'july' and date == 5:
        return 1
    else:
        return 0
    
month = input('Enter your month of birthday: ')
date = int(input('Enter your date of birth(day): '))
result = checkBirthday(month,date)
print(result)