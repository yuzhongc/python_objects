"""
@Time   :2021/10/26 20:48
@Author :Wesley
@File   :demo_c.PY
"""
import random


def fight(enemy_hp, enemy_power):
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    print(f"敌人的血量{enemy_hp},攻击力{enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp <= 0:
            print(f"我的剩余血量{my_hp}")
            print(f"敌人的剩余血量{enemy_hp}")
            print("I lost")
            break
        elif enemy_hp <= 0:
            print(f"我的剩余血量{my_hp}")
            print(f"敌人的剩余血量{enemy_hp}")
            print("I win")
            break


if __name__ == '__main__':
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    enemy_hp = random.choice(hp)
    enemy_power = random.randint(190, 210)
    fight(enemy_hp, enemy_power)







