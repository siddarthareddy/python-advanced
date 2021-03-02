from . import test


class A:
    def __init__(self):
        self.A1 = 10
        self.A2 = 20

    def resource(self):
        print("in resoruce")
        b = B(self.A1, self.A2)
        return b


class B:
    def __init__(self, A1, A2):
        self.A1 = A1
        self.A2 = A2

    def test_method(self):
        print("test method")
