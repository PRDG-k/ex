def avg_temp(weather_data):
    city = input("도시 이름을 입력하세요: ")
    filtered = list(filter(lambda x: x[1] == city, weather_data))
    print(f"{city}의 평균 기온: {sum(x[2] for x in filtered) / len(filtered):.2f}°C")
    print("")


def min_and_max_temp(weather_data):
    city = input("도시 이름을 입력하세요: ")
    filtered = list(filter(lambda x: x[1] == city, weather_data))
    print(f"{city}의 최고 기온: {max(x[2] for x in filtered):.1f}°C, 최저 기온: {min(x[2] for x in filtered):.1f}°C")
    print("")


def total_rainfall(weather_data):
    city = input("도시 이름을 입력하세요: ")
    filtered = list(filter(lambda x: x[1] == city, weather_data))
    print(f"{city}의 총 강수량: {sum(x[3] for x in filtered):.1f}mm")
    print(f"{city}의 강수량이 있었던 날: {sum(x[3] > 0 for x in filtered)}일")
    print("")


def add_data(weather_data):
    day = input("날짜를 입력하세요 (YYYY-MM-DD): ")
    city = input("도시 이름을 입력하세요: ")
    temp = input("평균 기온을 입력하세요(°C): ")
    rainfall = input("강수량을 입력하세요(mm): ")
    weather_data.append([day, city, float(temp), float(rainfall)])
    print(f"{city}의 날씨 데이터가 추가되었습니다.")
    print("")

    return weather_data

def print_data(weather_data):
    for data in weather_data:
        print(f"날짜: {data[0]}, 도시: {data[1]}, 평균 기온: {data[2]}°C, 강수량: {data[3]}mm")
    print("")


def menu():
    choice = input("원하는 기능의 번호를 입력하세요: ")
    if choice in ['1', '2', '3', '4', '5', '6']:
        return int(choice)
    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
        return -1

def Program(weather_data):
    print("1. 평균 기온 계산")
    print("2. 최고/최저 기온 찾기")
    print("3. 강수량 분석")
    print("4. 날씨 데이터 추가")
    print("5. 전체 데이터 출력")
    print("6. 종료")
    print("")
    while True:
        command = menu()
        if command == 1:
            avg_temp(weather_data)
        elif command == 2:
            min_and_max_temp(weather_data)
        elif command == 3:
            total_rainfall(weather_data)
        elif command == 4:
            weather_data = add_data(weather_data)
        elif command == 5:
            print_data(weather_data)
        elif command == 6:
            print("프로그램을 종료합니다.")
            return
        else:
            pass


if __name__ == '__main__':
    weather_data = [
        ["2023-01-01", "서울", 15.2, 0.0],
        ["2023-01-02", "부산", 18.4, 0.0],
        ["2023-01-03", "서울", 10.5, 2.3],
        ["2023-01-04", "부산", 14.6, 1.2],
        ["2023-01-05", "서울", 8.3, 0.0],
        ["2023-01-06", "부산", 12.0, 0.0],
    ]
    Program(weather_data)