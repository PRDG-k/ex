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
# name = input("이름을 입력하세요. ")
# age = input("나이를 입력하세요. ")
# print(f"안녕하세요! {name}님 ({age:^5})")

# # 2
# name = input("이름을 입력하세요. ")
# birth = int(input("태어난 연도를 입력하세요. "))
# year = int(input("올해 연도를 입력하세요. "))
# print(f"올해는 {year}, {name}님의 나이는 {year - birth + 1}세 입니다")

rainbow = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

# 1
# print(rainbow[2])
# # 2
# print(sorted(rainbow))
# # 3
# rainbow.append("white")
# print(rainbow)
# # 4
# del rainbow[2:6]
# print(rainbow)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# value = matrix[1][2]
# print(value)


# s1 = {1, 2, 3, 4}
# s3 = {3, 4, 5, 6}
# s2 = {4, 5, 6, 7}

# ans = s1 & s3 - s2
# print(ans)

# score = {}
# score.update({"Alice": 85, "Bob": 90, "Charlie": 95})
# score["David"] = 80
# score["Alice"] = 88
# del score["Bob"]

# print(score)

# 1
# PASSWORD = "abc123"
# _pw = input("비밀번호를 입력하세요: ")
# if _pw == PASSWORD:
#     print("비밀번호가 맞습니다")
# else:
#     print("비밀번호가 틀렸습니다")

# # 2
# num = int(input("숫자를 입력하세요: "))
# if num % 2 == 0:
#     print("짝수입니다")
# else:
#     print("홀수입니다")

# score = int(input("점수를 입력하세요: "))
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("학점:", grade)

age = int(input("나이를 숫자로 입력해주세요: "))
payment_method = input("결제방법을 입력해주세요 (현금 또는 카드): ")
fee = 0

if age < 8:
    fee = 0
elif age < 14:
    fee = 450
elif age < 20:
    if payment_method == "카드":
        fee = 720
    else:
        fee = 1000
elif age < 75:
    if payment_method == "카드":
        fee = 1200
    else:
        fee = 1300
else:
    fee = 0

print(f"{age}세의 {payment_method} 요금은 {fee}원입니다.")
