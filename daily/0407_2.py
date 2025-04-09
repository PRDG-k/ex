def Program():
    import random
    import time

    log = []
    words = ["mountain", "river", "forest", "ocean", "desert", "tree", "flower", "cloud", "rain", "sunlight"]
    repeat = False

    while True:
        if not repeat:
            word = random.choice(words)
            print(f"단어: {word}")
            start_time = time.perf_counter()
            repeat = True
        
        answer = input("입력: ")

        # while문 안에 받고 return하는 방법도 있다. exit조건을 두번 받지 않고 프로그램을 종료할 수 있음.
        if answer == "exit":
            print("게임 종료!")
            break

        if word == answer:
            end_time = time.perf_counter()
            log.append(end_time - start_time)
            print("통과!\n")
            repeat = False

        else:
            print("오타! 다시 시도하세요.\n")

    if log:
        total_time = sum(log)
        avg_time = sum(log) / len(log)
    else:
        total_time = 0
        avg_time = 0

    print(f"총 {len(log)}개의 단어를 입력하셨습니다.")
    print(f"총 걸린 시간: {total_time:4f}초")
    print(f"평균 단어당 입력시간 {avg_time:4f}초")


def Program2():
    import random
    import time

    log = []
    words = ["mountain", "river", "forest", "ocean", "desert", "tree", "flower", "cloud", "rain", "sunlight"]
    while True:
        word = random.choice(words)
        print(f"단어: {word}")
        start_time = time.perf_counter()
        
        while True:
            answer = input("입력: ")

            if answer == "exit":
                print("게임 종료!")
                if log:
                    total_time = sum(log)
                    avg_time = sum(log) / len(log)
                else:
                    total_time = 0
                    avg_time = 0

                print(f"총 {len(log)}개의 단어를 입력하셨습니다.")
                print(f"총 걸린 시간: {total_time:4f}초")
                print(f"평균 단어당 입력시간 {avg_time:4f}초")
                return

            if word == answer:
                end_time = time.perf_counter()
                log.append(end_time - start_time)
                print("통과!\n")
                break

            else:
                print("오타! 다시 시도하세요.\n")

if __name__ == "__main__":
    Program()