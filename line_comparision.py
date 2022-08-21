def calculate(x1, x2, y1, y2):
    return (x2-x1 ** 2 + y2-y1 ** 2) // 2


def compare(length):
    if length[0] == length[1]:
        print("Both are line are equal in length")
    else:
        print("Both are line are not equal in length")


if __name__ == "__main__":
    length = []
    print("Welcome to line comparison problem")
    for number in range(1, 3):
        print(f"Enter values of line {number}")
        x1 = int(input("Enter x1 point: "))
        x2 = int(input("Enter x2 point: "))
        y1 = int(input("Enter y1 point: "))
        y2 = int(input("Enter y2 point: "))
        length.append(calculate(x1, x2, y1, y2))
    compare(length)