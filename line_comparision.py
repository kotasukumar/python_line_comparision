class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.calculate(x1, x2, y1, y2)

    def calculate(x1, x2, y1, y2):
        return (x2 - x1 ** 2 + y2 - y1 ** 2) ** 0.5

    def compare(length):
        if length[0] > length[1]:
            print("Line 1 is greater then line 2")
        elif length[0] > length[1]:
            print("Line 2 is greater then line 1")
        elif length[0] == length[1]:
            print("Both are line are equal in length")
        else:
            print("Some where gone wrong please try again")


if __name__ == "__main__":
    length = []
    print("Welcome to line comparison problem")
    for number in range(1, 3):
        print(f"Enter values of line {number}")
        x1 = int(input("Enter x1 point: "))
        x2 = int(input("Enter x2 point: "))
        y1 = int(input("Enter y1 point: "))
        y2 = int(input("Enter y2 point: "))
        length.append(Line.calculate(x1, x2, y1, y2))
    print(length)
    Line.compare(length)
