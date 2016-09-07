if __name__ == '__main__':
    first, second = [int(x) for x in input().split(' ')]
    if first == second or first > second:
        print(first)
    else:
        print(second)
