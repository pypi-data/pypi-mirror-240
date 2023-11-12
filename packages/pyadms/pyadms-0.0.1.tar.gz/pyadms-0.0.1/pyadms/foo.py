
class A:
    def __init__(self):
        self.x = 5

    def printit(self):
        print(self.x)

class B(A):
    def __init__(self):
        super().__init__()

    def run(self):
        self.x = 4

b = B()
b.run()
print(b.x)
b.printit()
