from collections import Counter
import random
import time

def main():
    print(" ----- 50000 ")
    start = time.time()
    left, right = get_input(50000)
    run(left, right)
    print(f"Time Taken: {time.time() - start}")
    
    print(" ----- 250000 ")
    start = time.time()
    left, right = get_input(250000)
    run(left, right)
    print(f"Time Taken: {time.time() - start}")

    print(" ----- 1000000 ")
    start = time.time()
    left, right = get_input(1000000)
    run(left, right)
    print(f"Time Taken: {time.time() - start}")

    print(" ----- 10000000 ")
    start = time.time()
    left, right = get_input(10000000)
    run(left, right)
    print(f"Time Taken: {time.time() - start}")

    print(" ----- ")

def get_input(n):
    left = [random.randrange(10000, 99999, 1) for i in range(n)]
    right = [random.randrange(10000, 99999, 1) for i in range(n)]
    return left, right

def run(left, right):
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