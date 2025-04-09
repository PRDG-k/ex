try:
    x = int(input("숫자 입력:"))
    result = 10/ x
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("유효한 숫자가 아닙니다.")
except Exception as e:
    print(e)
else:
    print("결과:", result)
finally:
    print("프로그램 종료")