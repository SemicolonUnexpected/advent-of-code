path = "day_3_input.txt"


def one():
    file = open(path)
    text = file.read()

    i = 0
    while i < len(text):
        if text[i : i + 3] == "mul(":
            validMul = True
            # Step over the "mul("
            i += 3

            # Find the numbers
            a, b = 0, 0

            j = 0
            while j + i < len(text):
                if not text[i + j].isdigit():
                    validMul = False
                    i += j + 1
                    break

            if not validMul:
                break

            if text[i] != ",":
                


if __name__ == "__main__":
    one()
