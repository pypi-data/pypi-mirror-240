# Calculate binary numbers Addition
def processBinaryAddition(stringOne, stringTwo):
    try:
        # convert string binary to decimal
        decimalOne = convertBinaryToDecimal(stringOne)
        decimalTwo = convertBinaryToDecimal(stringTwo)
        
        addedDecimal = 0
        if isinstance(decimalOne, int) and isinstance(decimalTwo, int):
            addedDecimal = int(decimalOne + decimalTwo)
        else:
            addedDecimal = float(decimalOne + decimalTwo)
        
        # convert the result to binary 
        return convertDecimalToBinary(addedDecimal)
    except:
        return "Incorrect Binary Number: Can't process operation for incorrect binary number. Please put the correct binary number.\nAdvices: Surround your binary number with \"\". Example: \"10110\"."


# Calculate binary numbers Substraction
def processBinarySubtraction(stringOne, stringTwo):
    try:
        # convert string binary to decimal
        decimalOne = convertBinaryToDecimal(stringOne)
        decimalTwo = convertBinaryToDecimal(stringTwo)
        # substract them
        substractedDecimal = decimalOne - decimalTwo
        # convert the result to binary
        return convertDecimalToBinary(substractedDecimal)
    except:
        return "Incorrect Binary Number: Can't process operation for incorrect binary number. Please put the correct binary number.\nAdvices: Surround your binary number with \"\". Example: \"10110\"."
    

# Calculate binary numbers multiplication
def processBinaryMultiplication(stringOne, stringTwo):
    try: 
        # convert string binary to decimal
        decimalOne = convertBinaryToDecimal(stringOne)
        decimalTwo = convertBinaryToDecimal(stringTwo)
        # multiplicate them
        multiplicatedDecimal = decimalOne * decimalTwo
        # convert the result of binary
        return convertDecimalToBinary(multiplicatedDecimal)
    except:
        return "Incorrect Binary Number: Can't process operation for incorrect binary number. Please put the correct binary number.\nAdvices: Surround your binary number with \"\". Example: \"10110\"."


# Calculate binary numbers division, return two value: result and reminder
def processBinaryDivision(stringOne, stringTwo):
    try: 
        # convert string binary to decimal 
        decimalOne = convertBinaryToDecimal(stringOne)
        decimalTwo = convertBinaryToDecimal(stringTwo)
        dividedDecimal = 0
        reminderOfDividedDecimal = 0
        # divide them
        if isinstance(decimalOne, int) and isinstance(decimalTwo, int):
            dividedDecimal = int(decimalOne / decimalTwo)
            reminderOfDividedDecimal = int(decimalOne % decimalTwo)
        else:
            dividedDecimal = float(decimalOne / decimalTwo)
            reminderOfDividedDecimal = float(decimalOne % decimalTwo)

        return [convertDecimalToBinary(dividedDecimal), convertDecimalToBinary(reminderOfDividedDecimal)]
    except:
        return "Incorrect Binary Number: Can't process operation for incorrect binary number. Please put the correct binary number.\nAdvices: Surround your binary number with \"\". Example: \"10110\"."


# convert decimal number to binary
def convertDecimalToBinary(decimalNum):
    try: 
        dataTypeFloat = isinstance(decimalNum, float)
        dataTypeInt = isinstance(decimalNum, int)
        stringArrBinary = ""
        minus = False

        if decimalNum < 0:
            minus = True

        if dataTypeInt:
            decimalNumber = int(decimalNum)
            if decimalNumber < 0:
                minus = True
            arrBinary = []
            while decimalNumber != 0:
                arrBinary.insert(0,decimalNumber % 2)
                decimalNumber = int(decimalNumber / 2)
            
            for i in arrBinary:
                stringArrBinary += str(i)
            
            if stringArrBinary == "":
                stringArrBinary += "0"

            if minus:
                stringArrBinary = "-" + stringArrBinary

        if dataTypeFloat:
            numInFrontOfPoint = int(decimalNum)
            decimalNum = int(decimalNum * pow(2,8))
            frontOfPoint = []
            behindOfPoint = []

            if minus:
                while decimalNum < numInFrontOfPoint:
                    remainder = decimalNum % 2
                    if remainder == 0:
                        behindOfPoint.append('0')
                    elif remainder == 1:
                        behindOfPoint.append('1')
                    decimalNum = int(decimalNum/2)

                while decimalNum < 0:
                    remainder = decimalNum % 2
                    if remainder == 0:
                        frontOfPoint.append('0')
                    elif remainder == 1:
                        frontOfPoint.append('1')
                    decimalNum = int(decimalNum/2)
            else:
                while decimalNum > numInFrontOfPoint:
                    remainder = decimalNum % 2
                    if remainder == 0:
                        behindOfPoint.append('0')
                    elif remainder == 1:
                        behindOfPoint.append('1')
                    decimalNum = int(decimalNum/2)

                while decimalNum > 0:
                    remainder = decimalNum % 2
                    if remainder == 0:
                        frontOfPoint.append('0')
                    elif remainder == 1:
                        frontOfPoint.append('1')
                    decimalNum = int(decimalNum/2)

            frontReverse = []
            behindReverse = []
            [frontReverse.append(frontOfPoint[i]) for i in range(len(frontOfPoint)-1, -1, -1)]
            [behindReverse.append(behindOfPoint[j]) for j in range(len(behindOfPoint)-1, -1, -1)]

            for i in frontReverse:
                stringArrBinary = stringArrBinary + i
            
            stringArrBinary = stringArrBinary + "."

            for j in behindReverse:
                stringArrBinary = stringArrBinary + j

            if stringArrBinary == "":
                stringArrBinary += "0"

            if minus:
                stringArrBinary = "-" + stringArrBinary

        return stringArrBinary
    except:
        return "Incorrect Decimal Number: Can't process operation for incorrect decimal number. Please put the correct decimal number."


# convert binary number to decimal
def convertBinaryToDecimal(binary):
    try: 
        minus = False
        isFloat = False
        total = 0
        if binary[0] == "-":
            minus = True
        
        binaryNumberBeforePoint = ""
        binaryNumberAfterPoint = ""

        for i in binary:
            if i == '.':
                isFloat = True

        if isFloat:
            splittedNumber = binary.split(".")
            binaryNumberBeforePoint = splittedNumber[0]
            
            binaryNumberAfterPoint = splittedNumber[1]
            

            reverseBinaryNumberBeforePoint = []
            [reverseBinaryNumberBeforePoint.append(binaryNumberBeforePoint[i]) for i in range(len(binaryNumberBeforePoint)-1, -1, -1)]
            if reverseBinaryNumberBeforePoint[len(reverseBinaryNumberBeforePoint)-1] == '-':
                reverseBinaryNumberBeforePoint.pop(len(reverseBinaryNumberBeforePoint)-1)

            for j in range(len(reverseBinaryNumberBeforePoint)-1, -1, -1):
                k = float(reverseBinaryNumberBeforePoint[j]) * pow(2,j)
                total = total + k
            for l in range(0, len(binaryNumberAfterPoint)):
                k = float(binaryNumberAfterPoint[l]) * pow(2,(-1 * (l + 1)))
                total = total + k
        else:
            reverseBinary = []
            [reverseBinary.append(binary[i]) for i in range(len(binary)-1, -1, -1)]
            if reverseBinary[len(reverseBinary)-1] == "-":
                reverseBinary.pop(len(reverseBinary)-1)
            for i in range(len(reverseBinary)-1,-1,-1):
                j = int(reverseBinary[i]) * pow(2, i)
                total = total + j
        
        if minus:
            total = -1 * total
        return total
    except:
        return "Incorrect Binary Number: Can't process operation for incorrect binary number. Please put the correct binary number.\nAdvices: Surround your binary number with \"\". Example: \"10110\"."