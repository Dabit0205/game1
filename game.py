import os
import random
import time
import Character


def ending(monster):
    print("게임 Over")
    print(f"{monster.name}에게 죽었다.")

    time.sleep(2)
    os.system('cls||clear')

# 전투 상황


def battle(player, monster):
    monster = create_monster()
    print(f"{monster.name}를 마주쳣다.")
    print('전투 시작!')

    while (True):
        os.system('cls||clear')
        print(f"{[player.name]} HP :{[player.max_hp]} MP :{[player.max_mp]}")
        print(f"{[monster.name]}: {[monster.max_hp]}\n")

        # 공격 타입 선택
        print("어떤 공격을 사용하시겠습니까?")
        print("1. 일반공격 2. 마법공격")
        attack_type = input("번호를 입력하세요 >> ")

        # 플레이어의 공격
        if attack_type == '1':
            player.normal_power(monster)
        elif attack_type == '2':
            player.magic_power(monster)
        else:
            print("잘못된 입력입니다.")
            os.system("pause")
            continue

        if player.now_hp <= 0 or monster.now_hp <= 0:
            return 0
        else:
            monster.normal_attack(player)
            if player.now_hp <= 0 or monster.now_hp <= 0:
                return 0
        os.system("pause")

        monster.now_hp -= damage
        if monster.now_hp <= 0:
            print(f"{player.name}이(가) {monster.name}을(를) 물리쳤습니다!")
            break

        # 몬스터의 공격
        damage = random.randint(monster.normal_power - 2,
                                monster.normal_power + 2)
        player.now_hp -= damage
        if player.now_hp <= 0:
            print(f"{monster.name}이(가) {player.name}을(를) 물리쳤습니다!")
            break

    print('전투 종료!')
    if player.now_hp > 0:
        print(f"{player.name}이(가) 승리했습니다!")
    else:
        print(f"{monster.name}이(가) 승리했습니다!")
        print("GAME OVER")


def start():
    # os.system('cls||clear')
    name = input("내 이름은 >>")
    Player = Character.CreateUser(
        name, hp=500, normal_power=20, mp=200, magic_power=40)

    Monster = Character.CreateMonster(
        name,  hp=100, normal_power=20
    )

    print(f'내 이름은 {Player.name}이다.')

    time.sleep(1.5)

    i = choice("start")

    os.system("pause")
    while (True):
        os.system('cls||clear')
        i = choice("select")
        if i == '1':
            if Player.now_hp >= 0:
                print("3입니다.")

        elif i == '2':
            Player.show_status()
            time.sleep(2)
        else:
            print("잘못된 입력입니다.")


# 몬스터 생성


def create_monster():
    names = ["달팽이", "주황버섯", "슬라임"]
    monster_name = random.choice(names)
    print(f"Selected name: {monster_name}")


def choice(scene):
    while (True):
        if scene == "start":
            cmd = input("계속하려면 1, 종료하려면 2>>")

            if cmd == '1':
                return cmd
            elif cmd == '2':
                print("종료.")
                break
            else:
                print("잘못된 입력입니다.")
                return cmd

        elif scene == "select":
            print("1. 전투하기")
            print("2. 상태확인")
            cmd = input("무엇을 할까? >> ")
            if cmd == '1':
                print("1 입력입니다")
            elif cmd == '2':
                print("2 입력입니다.")
            else:
                print("잘못된 입력입니다.")
