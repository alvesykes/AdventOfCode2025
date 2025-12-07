def checkRepeatedSequences(start, end):
    result = 0
    for number in range(start, end + 1):
        num_str = str(number)
        length = len(num_str)
        print(num_str[0:length//2], num_str[length//2:])
        if(num_str[0:length//2] == num_str[length//2:]):
            result += number
    return result

def main():
    result = 0

    with open('input.txt') as file:
        for line in file:
            parts = line.strip().split(',')
            for part in parts:
                if '-' in part:
                    start_str, end_str = part.split('-')
                    start = int(start_str)
                    end = int(end_str)
                    result += checkRepeatedSequences(start, end)      
    print(result)
    file.close()

main()