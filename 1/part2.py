def count_zeros_R(pos, d):
    first = (100 - pos) % 100
    if first == 0:
        first = 100  

    if d < first:
        return 0

    return 1 + (d - first) // 100


def count_zeros_L(pos, d):
    first = pos % 100
    if first == 0:
        first = 100  

    if d < first:
        return 0

    return 1 + (d - first) // 100


def main():
    pos = 50 
    total_zeros = 0

    with open("input.txt") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            d = int(line[1:])

            if direction == 'R':
                total_zeros += count_zeros_R(pos, d)
                pos = (pos + d) % 100

            else:  # 'L'
                total_zeros += count_zeros_L(pos, d)
                pos = (pos - d) % 100

    print(total_zeros)


main()
