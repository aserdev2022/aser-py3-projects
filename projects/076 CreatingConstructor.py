class Operation:
    def __init__(self, a, b):
        print("Constructor called")
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)


o1 = Operation(20, 30)
o1.add()

o2 = Operation(10, 30)
o2.add()
