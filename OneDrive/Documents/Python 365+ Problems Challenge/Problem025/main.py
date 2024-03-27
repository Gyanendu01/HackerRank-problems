def tempCalculate(celcius):
    result = (celcius * 9//5) + 32
    return result

print(tempCalculate(float(input('Enter the temperature in celcius: '))))
