import math

if __name__ == '__main__':
    number = int(input())

    sqrt = math.sqrt(number)
    high_factorial = math.floor(sqrt)

    numbers = []
    total = 0

    while total != number:
        current_fat = math.factorial(high_factorial)
        if current_fat + total <= number:
            total += current_fat
            numbers.append(high_factorial)
        elif high_factorial > 1:
            high_factorial -= 1

    print(len(numbers))
