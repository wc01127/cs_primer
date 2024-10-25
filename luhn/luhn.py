"""
-Write a function verify(digits) -> true/fals which validates a string of digit characters
-The final digit will be the check digit. Iterate through others in reverse order
    doubling each second digit starting from the rightmost non-check digit, adding 
    together the resulting digits, combining to compute a total which should
    be 10 - checkdigit mod 10
-Testing strategyL verify


"""


def luhnAlgo(thisNum):
    checkSum = thisNum % 10
    newNum = int(thisNum/10)
    iterateNum = str(newNum)
    numDigits = len(iterateNum)
    sumLuhnDig = 0
    for i in range(numDigits-1, -1, -1):
        if ((numDigits-1)-i) == 0 or ((numDigits-1)-i) % 2 == 0:
            multDig = int(iterateNum[i]) * 2
            newDig = str(multDig)
            sumDig = 0
            for j in range(2):
                sumDig += int(newDig[j])
            sumLuhnDig += sumDig
        else:
            sumLuhnDig += int(iterateNum[i])
    print(sumLuhnDig)
    print(checkSum)
    validateLuhn = (10 - (sumLuhnDig % 10)) % 10
    print(validateLuhn)
    if checkSum == validateLuhn:
        print('TRUE')
    else:
        print('FALSE')

luhnAlgo(17893729974)