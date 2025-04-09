# with open("user_input.txt", "w", encoding="utf-8") as file:
#     file.write("Hello\n")
#     file.write("파이썬 파일 쓰기 연습.")

# with open("user_input.txt", "a", encoding="utf-8") as file:
#     file.write("\n내용추가")
#     # write는 문자열 형태만 가능
#     # file.write(12345)   # TypeError! write() argument must be str, not int
#     file.write("\n12345")


# 여러개를 한번에 추가
# from itertools import repeat, chain
# lines = ["1", "2", "3", "4", "5"]
# line_sep = repeat("\n")
# with open("list.txt", "w", encoding="utf-8") as file:
#     line_iter = chain.from_iterable(zip(lines, line_sep))
#     file.writelines(line_iter)

# with open("input.txt", "w", encoding="utf-8") as file:
#     while True:
#         line = input("파일에 저장할 내용을 입력하세요: ")
#         if line == "종료":
#             print("입력 종료")
#             break

#         file.write(line + "\n")
#     print("저장 성공")

with open("img/camel.jpeg", "rb") as file:
    # data = file.read()
    # print(f"{len(data)} Byte")
    header = file.read(10)
    print(header)

def identify_file(file_name):
    with open(file_name, "rb") as file:
        header = file.read(10)
        print(header)

        if header[:2] == b'x\ff\xd8':
            return "JPEG"
        elif header == b'\x89PNG':
            return "PNG"
        else:
            return "Unknown"