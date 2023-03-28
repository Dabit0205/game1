import os
import time
import game


def game_start():
    # os.system('cls||clear')
    print("Start Game")
    time.sleep(2)
    # os.system('cls||clear')
    opening()


def opening():

    while (True):
        print("1. 게임 시작")
        print("2. 게임 종료")
        uinput = input(">>")
        if uinput == '1':
            game.start()
        elif uinput == '2':
            break
        else:
            print("잘못된 값입니다.")


if __name__ == "__main__":
    game_start()
