def checkRepeatedSequences(start, end):
    result = 0
    for number in range(start, end + 1):
        num_str = str(number)
        length = len(num_str)
        
        is_invalid = False
        for pattern_len in range(1, length):
            if length % pattern_len == 0:
                pattern = num_str[:pattern_len]
                if pattern * (length // pattern_len) == num_str:
                    is_invalid = True
                    break
        
        if is_invalid:
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