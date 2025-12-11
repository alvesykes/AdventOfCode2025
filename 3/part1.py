def checkSequences(line):
    firstDigit = 0
    secondDigit = 0
    result = 0
    
    for i in range(len(line)):
        if line[i] == '\n':
            break
        if int(line[i]) > firstDigit:
            firstDigit = int(line[i])
            secondDigit = 0
            for j in range(i + 1, len(line)):
                if line[j] == '\n':
                    break
                if int(line[j]) > secondDigit:
                    secondDigit = int(line[j])
                    resultTemp = firstDigit * 10 + secondDigit
        if resultTemp > result:
            result = resultTemp
    print(f"Line: {line.strip()} - Result: {result}")
    return result

def main():
    finalResult = 0
    with open('input.txt') as file:
        for line in file:
            finalResult += checkSequences(line)
    print(finalResult)
    file.close()

main()