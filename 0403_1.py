# 실습 1
class TwoNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        _result = []
        if self.b == 0:
            return "0으로 나눌 수 없습니다."
        return self.a / self.b

a, b = map(int, input("두 개의 숫자를 입력하세요: ").split())
num = TwoNum(a, b)
print(f"덧셈: {num.add()}")
print(f"뺄셈: {num.sub()}")
print(f"곱셈: {num.mul()}")
print(f"나눗셈: {num.div()}")

num2 = TwoNum(3, 4)
print(f"덧셈: {num + num2}")