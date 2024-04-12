class Calculator():
    def __init__(self):
        self.value1 = None
        self.value2 = None

    def UserInput(self):
        try:
            self.value1 = float(input("Enter first value: "))
            self.value2 = float(input("Enter second value: "))
            calculate = input("Type of calculation (e.g division,addition): ")
        except Exception as e:
            print(f"An error occured {e}.")

        if calculate.lower() == 'addition' or calculate.lower() == 'add':
            self.add()
        elif calculate.lower() == 'division' or calculate.lower() == 'divide':
            self.divide()
        elif calculate.lower() == 'multiplication' or calculate.lower() == 'multiply':
            self.multiply()
        elif calculate.lower() == 'subtraction' or calculate.lower() == 'subtract':
            self.subtract()
        elif calculate.lower() == 'module':
            self.module()
        elif calculate == '':
            print('Select the calculation type.')
        else:
            print('Invalid input')


    def add(self):
        result = self.value1 + self.value2
        print(result)
    def divide(self):
        if self.value2 != 0:
            result = self.value1 / self.value2
            print(result)
        else:
            print('Cannot divide by zero.')
    def multiply(self):
        result = self.value1 * self.value2
        print(result)
    def subtract(self):
        result = self.value1 - self.value2
        print(result)
    def module(self):
        result = self.value1 % self.value2
        print(result)

calc = Calculator()
calc.UserInput()
