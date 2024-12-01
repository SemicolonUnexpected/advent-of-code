from collections import Counter


path = 'day_1_input.py'


def one():
    file = open(path)
    lines = file.read().split('\n')[:-1]

    left = sorted([int(line[:5]) for line in lines])
    right = sorted([int(line[8:]) for line in lines])

    sum = 0
    for i in range(len(left)):
        sum += abs(left[i] - right[i])

    print(sum)


def two():
    file = open(path)
    lines = file.read().split('\n')[:-1]

    left = sorted([int(line[:5]) for line in lines])
    right = Counter([int(line[8:]) for line in lines])

    similarity = 0
    for number in left:
        similarity += number * right.get(number, 0)

    print(similarity)


if __name__ == "__main__":
    two()
