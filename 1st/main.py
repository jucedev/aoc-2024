def main():
    with open("input.txt", "r") as input_file:
        input_list = input_file.readlines()

    left = []
    right = []

    for row in input_list:
        split = row.split("   ")
        left.append(int(split[0]))
        right.append(int(split[1].rstrip()))

    left = sorted(left)
    right = sorted(right)

    distance = 0
    similarity = 0
    for i in range(len(left)):
        l = left[i]
        r = right[i]

        if (l > r):
            distance += l - r
        else:
            distance += r - l

        count = right.count(l)
        similarity += l * count

    print("distance:", distance)
    print("similarity:", similarity)
    
if __name__ == '__main__':
    main()