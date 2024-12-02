path = 'day_2_input.txt'


def one():
    file = open(path)
    data = [
            [int(value) for value in line.split(' ')]
            for line in file.read().split('\n')[:-1]
            ]

    sum = 0
    for report in data:
        isDescending = report[0] > report[1]
        for i in range(len(report) - 1):
            diff = report[i] - report[i + 1]

            if diff < 0 and not isDescending:
                break



if __name__ == "__main__":
    one()
