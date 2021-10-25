"""
@Time   :2021/10/26 20:25
@Author :Wesley
@File   :demo_a_1026.PY
"""

"""
回合制游戏：每个角色都有hp和power，hp代表血量，power代表攻击力
hp的初始值未1000，power的初始值为200。
定义一个fight方法
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
函数
循环/判断
三母运算
类型提示
"""


# 定义fight函数实现游戏逻辑
def fight():
    # 定义4个变量存放数据
    my_hp = 1000
    my_power = 200
    enemy_hp = 1000
    enemy_power = 200
    # 定义最终血量计算方式
    my_final_hp = my_hp - enemy_power
    enemy_final_hp = enemy_hp - my_power

    # 判断输赢
    # if my_final_hp > enemy_final_hp:
    #     print("I win")
    # elif my_final_hp < enemy_final_hp:
    #     print("Enemy win")
    # else:
    #     print("All win")

    # 三母运算，与if-else，只是语法简洁了
    print("I win") if my_final_hp > enemy_final_hp else print("I lost")


fight()









