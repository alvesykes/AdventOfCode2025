def rotateR(x, i):
    if x + i > 99:
        i = x + i - 100
    else:
        i += x
    while  i > 99:
        i -= 100
    return i

def rotateL(x, i):
    if i - x < 0:
        i = 100 + (i - x) 
    else:
        i -= x
    while i < 0:
        i += 100
    return i

def main():
    i = 50
    result = 0
    with open('input.txt') as file:
        for line in file:
            res = []
            for ch in line:
                if ch.isdigit():
                    res.append(int(ch))
            numb = 0
            if len(res) == 1:
                numb = res[0] * 1
            if len(res) == 2:
                numb= res[0] * 10 + res[1] * 1
            if len(res) == 3:
                numb= res[0] * 100 + res[1] * 10 + res[2] * 1
            if line[0] == 'L':
                i = rotateL(numb, i)
            if line[0] == 'R':
                i = rotateR(numb, i)
            if i == 0:
                result +=1
    print(result)
    file.close()

main()