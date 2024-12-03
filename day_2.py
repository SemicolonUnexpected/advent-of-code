path = "day_2_input.txt"


def one():
    file = open(path)
    data = [
        [int(value) for value in line.split(" ")]
        for line in file.read().split("\n")[:-1]
    ]

    # data = [[7, 6, 4, 2, 1]]

    sum = 0
    for report in data:
        isDescending = report[0] > report[1]
        print(isDescending)
        for i in range(len(report) - 1):
            diff = report[i + 1] - report[i]

            if diff < 0 and not isDescending:
                # print(f"The sequence is going the wrong way (not decreasing): {report}")
                break

            if diff > 0 and isDescending:
                # print(f"The sequence is going the wrong way (not increasing): {report}")
                break

            if abs(diff) == 0 or abs(diff) > 3:
                # print(f"The sequence is jumping too much: {report}")
                break

            if i == len(report) - 2:
                # print(f"Sequence just right: {report}")
                sum += 1

    print(sum)


def two():
    file = open(path)
    data = [
        [int(value) for value in line.split(" ")]
        for line in file.read().split("\n")[:-1]
    ]

    # data = [[7, 6, 4, 2, 1]]
    report = [7, 6, 4, 2, 1]



def check_with_error(report):
    noError = True
    errorPosition = None
    isDescending = report[0] > report[1]

    # Pointer moving to the right
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if diff < 0 and not isDescending:
            noError = False
            errorPosition = i
            break

        if diff > 0 and isDescending:
            noError = False
            errorPosition = i
            break

        if abs(diff) == 0 or abs(diff) > 3:
            noError = False
            errorPosition = i
            break

    return noError or check_with_error(report[:

    # Pointer moving left
    for i in range(len(report) - 1, 0, -1):
        print(i)


if __name__ == "__main__":
    two()
