"""
@Time   :2021/10/26 20:42
@Author :Wesley
@File   :demo_b.PY
"""


def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 199

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        if my_hp <= 0:
            print("I lost")
            break
        elif enemy_hp <= 0:
            print("I win")
            break

fight()



