# print("Hello", "Python")
# print("Hello", "Python", end="***")
# print((100-2)/7+9*3)
# print("안녕하세요")

# c = 3 + 4j
# print(c.real)
# print(c.imag)
# print(c.conjugate())
# print(abs(c))
# print(type(c))
# "오브젝트는 타입의 인스턴스"
# print(type(object))

# x = 5
# print(3 < x == 5)   # True (x가 5일 때)
# print(3 < (x == 5))  # False (x == 5가 먼저 평가됨)

# from sys import getsizeof

# print(getsizeof(0))
# print(getsizeof(1))
# print(getsizeof(2**30))
# print(getsizeof(2**1000))
# print(getsizeof(2**10000))
# print(getsizeof(2**100000))
# print(getsizeof(2**1000000))
# print(getsizeof(2**10000000))
# OverflowError: int too large to convert to float

# print("|\\_/|")
# print("|q p|   /}")
# print("( 0 )\"\"\"\\")
# print("|\"^\"`    |")
# print("||_/=\\\\__|")


# print(f"문자열 실습입니다. {{{"강민규":=^5}}}를 출력해보세요.")


# char = '"'

# dog = "|\_/| %6s" % ""
# print(dog)
# dog = "|q p| %4s/}" % ""
# print(dog)
# dog = "({0:^3})".format(0)
# dog1 = "{0:{char}>5}" .format("\\", char=char)
# dog2 = dog + dog1
# print(dog2)

# 1
name = input("이름을 입력하세요. ")
age = input("나이를 입력하세요. ")
print(f"안녕하세요! {name}님 ({age:^5})")

# 2
name = input("이름을 입력하세요. ")
birth = int(input("태어난 연도를 입력하세요. "))
year = int(input("올해 연도를 입력하세요. "))
print(f"올해는 {year}, {name}님의 나이는 {year - birth + 1}세 입니다")
