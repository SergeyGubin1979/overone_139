class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def func_1(self):
        return self.a + self.b

    def func_2(self):
        return self.a - self.b

    def func_3(self):
        return self.a - self.b
    def func_4(self):
        if self.b == 0:
            return 'error'
        else:
            return self.a / self.b
while True:
    print("Действие")
    x = input()
    a = int(input())
    b = int(input())

    example = Example(a, b)
    if x =='+':
        print(example.func_1())
    elif x =='-':
        print(example.func_2())
    elif x =='*':
        print(example.func_3())
    elif x =='/':
        print(example.func_4())


