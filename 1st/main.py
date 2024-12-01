from collections import Counter
import time

def main():
    start = time.time()
    run()
    print(f"Time Taken: {time.time() - start}")

def run():
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
    for i in range(len(left)):
        l = left[i]
        r = right[i]

        if (l > r):
            distance += l - r
        else:
            distance += r - l

    right_counter = Counter(right)
    similarity =  sum(l * right_counter[l] for l in left)

    print("distance:", distance)
    print("similarity:", similarity)
    
if __name__ == '__main__':
    main()