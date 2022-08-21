def calculate(x1, x2, y1, y2):
    return (x2-x1 ** 2 + y2-y1 ** 2) // 2


print("Welcome to line comparison problem")
x1 = int(input("Enter x1 point: "))
x2 = int(input("Enter x2 point: "))
y1 = int(input("Enter y1 point: "))
y2 = int(input("Enter y2 point: "))
print(calculate(x1, x2, y1, y2))