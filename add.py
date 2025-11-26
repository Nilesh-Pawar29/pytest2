def add(a, b):
    return a + b
import sys
if __name__ == "__main__":
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum:", add(num1, num2))