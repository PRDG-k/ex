# # # # # 창고 정리
# # # # def solution(storage, num):
# # # #     clean_storage = []
# # # #     clean_num = []
# # # #     for i in range(len(storage)):
# # # #         if storage[i] in clean_storage:
# # # #             pos = clean_storage.index(storage[i])
# # # #             clean_num[pos] += num[i]
# # # #         else:
# # # #             clean_storage.append(num[i])
# # # #             clean_num.append(num[i])

# # # #     # 아래 코드에는 틀린 부분이 없습니다.

# # # #     max_num = max(clean_num)
# # # #     answer = clean_storage[clean_num.index(max_num)]
# # # #     return answer


# # # # solution(["pencil", "pencil", "pencil", "book"], [2, 4, 3, 1])


# # # # def Program(a, b):
# # # #     if a == b:
# # # #         print("결과(곱):", a * b)
# # # #     else:
# # # #         print("결과(합):", a + b)


# # # # Program(2, 2)
# # # # Program(2, 3)

# # # # def Program(price):
# # # #     if price < 20000:
# # # #         return price + 2500
# # # #     else:
# # # #         return price


# # # # item = [30000, 15000]
# # # # for i in range(len(item)):
# # # #     print(f"상품{i} 가격: {Program(item[i])}원")


# # # # [].index("a")

# # # # def Program(num):
# # # #     li = [i for i in range(num, 30+1, num)]
# # # #     print(" ".join(map(str, li)))
# # # #     print(f"{num}의 배수의 개수: {len(li)}")

# # # # li = [i for i in range(1, 30+1) if i % num == 0]
# # # # print(f"{num}의 배수의 개수: {len(li)}")

# # # # # or
# # # # li = filter(lambda x: x % num == 0, range(1, 30+1))
# # # # print(f"{num}의 배수의 개수: {len(list(li))}")

# # # # # or
# # # # li = [i for i in range(num, 30+1, num)]
# # # # print(f"{num}의 배수의 개수: {len(li)}")


# # # # Program(3)


# # # # def sos(i):
# # # #     print("Help me!")
# # # #     if i == 1:
# # # #         return ""
# # # #     else:
# # # #         return sos(i-1)
# # # # sos(10)


# # # def factorial(i):
# # #     if i == 1:
# # #         return 1
# # #     else:
# # #         return i * factorial(i-1)


# # # print(factorial(5))  # 120




# def Program(num):
#     numbers = list(range(1, 31))
#     filtered = list(filter(lambda x: x % num == 0, numbers))
#     print(" ".join(map(str, filtered)))
#     print(f"{num}의 배수의 개수: {len(filtered)}")