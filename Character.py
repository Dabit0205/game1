import random

# 캐릭터 기본 베이스


class Character:

    # 일반 공격
    def normal_attack(self, other):
        # 공격력 범위 내에서 랜덤한 데미지를 계산
        damage = int(random.randint(
            self.normal_power-10, self.normal_power+10))
        # 상대방의 체력을 감소시키고 출력
        other.now_hp = max(other.max_hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        # 상대방의 체력이 0이 되면 쓰러짐을 출력
        if other.now_hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    # 캐릭터 상태 확인
    def show_status(self):
        print(f"{self.name}의 상태")
        print(f"HP {self.now_hp}/{self.max_hp}")


# 유저 캐릭터 생성
class CreateUser(Character):

    # 이름, 최대 체력, 현재 체력, 일반 공격력, 최대 마력, 현재 마력, 마법 공격력
    def __init__(self, name, normal_power, magic_power, hp=None, mp=None):
        self.name = name
        self.max_hp = hp or 500
        self.now_hp = self.max_hp
        self.max_mp = mp or 200
        self.now_mp = self.max_mp
        self.normal_power = normal_power
        self.magic_power = magic_power

    # 마법 공격
    def magic_attack(self, other):
        # 공격력 범위 내에서 랜덤한 데미지를 계산
        damage = int(random.randint(self.magic_power, self.magic_power+20))
        # 상대방의 체력을 감소시키고 출력
        other.now_hp = max(other.max_hp - damage, 0)
        print(f"{self.name}의 마법 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")

        # 마법 공격으로 인한 마나 감소
        self.now_mp = max(self.max_mp - 40, 0)

        # 상대방의 체력이 0이 되면 쓰러짐을 출력
        if other.now_hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    # 유저 캐릭터의 상태를 출력
    def show_status(self):
        print(f"{self.name}의 상태")
        print(f"HP {self.now_hp}/{self.max_hp}")
        print(f"HP {self.now_mp}/{self.max_mp}")


# 몬스터 캐릭터 생성
class CreateMonster(Character):

    # 이름, 최대 체력, 현재 체력, 공격력

    def __init__(self, name, normal_power, hp=None):
        self.name = name
        self.max_hp = hp or 100
        self.now_hp = self.max_hp
        self.normal_power = normal_power
