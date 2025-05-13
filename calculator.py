class Calculator:
    def add(self, x, y):
        return x + y
        
    def substract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y
        
if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
    print("Current feature: Addition")
    print("Example: 5 + 3 =", calc.add(5, 3))
    print("Example: 9 - 4 =", calc.substract(9, 4))
    print("Example: 5 * 8 =", calc.multiply(5, 8))
