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

# rainbow = ["red", "orange", "yellow", "green", "blue", "navy", "purple"]

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

# age = int(input("나이를 숫자로 입력해주세요: "))
# payment_method = input("결제방법을 입력해주세요 (현금 또는 카드): ")
# fee = 0

# if age < 8:
#     fee = 0
# elif age < 14:
#     fee = 450
# elif age < 20:
#     if payment_method == "카드":
#         fee = 720
#     else:
#         fee = 1000
# elif age < 75:
#     if payment_method == "카드":
#         fee = 1200
#     else:
#         fee = 1300
# else:
#     fee = 0

# print(f"{age}세의 {payment_method} 요금은 {fee}원입니다.")

# calories = {"apple": 95, "banna": 105, "cherry": 50}
# fruit = input("과일 이름을 영문으로 입력하세요: ")

# if fruit in calories:
#     print(f"{fruit}의 칼로리는 {calories[fruit]}kcal 입니다.")
# else:
#     print(f"{fruit}는 없는 과일입니다.")

# while True:
#     num = input("숫자를 입력하세요: ")
#     if num.isdigit():
#         num = int(num)
#     else:
#         print("숫자만 입력하세요.")
#         continue

#     if num == 0:
#         continue
#     elif num > 0:
#         print(f"1부터 {num}까지의 합은 {(num * (1+num))/2}입니다.")
#         break
#     else:
#         print("양수만 입력하세요.")

# 1
# num = int(input("숫자를 입력하세요: "))
# for i in range(1, 10):
#     print(f"{num} x {i} = {num*i}")

# # 2
# num = int(input("숫자를 입력하세요: "))
# sum = 0
# for i in range(1, num+1, 2):
#     sum += i
# print(f"1부터 {num}까지의 홀수의 합: {sum}")

# 3
# students = {
#     "학생1": {"국어": 83, "영어": 92, "수학": 88},
#     "학생2": {"국어": 90, "영어": 79, "수학": 86},
#     "학생3": {"국어": 88, "영어": 86, "수학": 94},
# }

# for student, scores in students.items():
#     avg_score = sum(scores.values()) / len(scores)
#     print(f"{student}의 평균 점수는 {avg_score:.2f}입니다.")


# tables = [[i * j for i in range(1, 10)] for j in range(1, 10)]
# for i in range(1, 10):
#     print(f"[{i}단]")
#     for j in range(1, 10):
#         print(f"{i} x {j} = {i*j}")
#         # print(f"{i} x {j} = {tables[i-1][j-1]}")
#     print()


def check_machine(vending_machine):
    print("남은 음료수: ", vending_machine)


def is_drink(item, vending_machine):
    if item in vending_machine:
        return True
    else:
        return False


def add_drink(vending_machine):
    item = input("음료를 입력하세요: ")
    if is_drink(item, vending_machine):
        idx = vending_machine.index(item)
        vending_machine.insert(idx, item)
    else:
        vending_machine.append(item)
    print("추가 완료")
    check_machine(vending_machine)
    return vending_machine


def remove_drink(vending_machine):
    item = input("삭제할 음료수? ")
    if is_drink(item, vending_machine):
        vending_machine.remove(item)
        print("삭제 완료")
    else:
        print("음료가 없습니다.")

    check_machine(vending_machine)
    return vending_machine


vending_machine = ["게토레이", "게토레이", "레쓰비", "레쓰비", "생수", "생수", "생수", "이프로"]
isOwner = False

while True:
    print("사용자 종류를 입력하세요:")
    print("1. 소비자")
    print("2. 주인")
    user = input()
    if user.isdigit():
        if int(user) == 1:
            user = "소비자"
        elif int(user) == 2:
            user = "주인"

    if user == "주인":
        isOwner = True
        break
    elif user == "소비자":
        isOwner = False
        break
    else:
        print("올바른 명령을 입력하세요.")

if isOwner:
    print("할 일 선택")
    print("1. 추가")
    print("2. 삭제")
    command = input()

    if command.isdigit():
        if int(command) == 1:
            command = "추가"
        elif int(command) == 2:
            command = "삭제"

    if command == "추가":
        vending_machine = add_drink(vending_machine)
    elif command == "삭제":
        vending_machine = remove_drink(vending_machine)
    else:
        print("올바른 명령을 입력하세요.")
else:
    order = input("마실 음료는?: ")
    vending_machine = remove_drink(order)
    print(f"{order} 나왔습니다.")
