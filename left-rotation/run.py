from rotLeft import rotLeft

if __name__ == "__main__":
    # Accept n and d
    print("Enter the length of your list and the number of left-rotations as two numbers, space-separated:")
    n, d = list(map(int, input().split()))
    print(f'n = {n}')
    print(f'd = {d}')

    # Create list of integers 1 -> n
    a = list(range(1, n + 1))
    print(f'a = {a}')

    print(f'Left rotated array of n integers d times: {rotLeft(a, d)}')
