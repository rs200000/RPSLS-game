#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：冉松
日期：2021.11.25
"""
import random

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=='石头':
        number=0
    elif name=='史波克':
        number=1
    elif name=='布':
        number=2
    elif name=='蜥蜴':
        number=3
    elif name=='剪刀':
        number=4
    return number

def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
       name='石头'
    elif number==1:
         name='史波克'
    elif number==2:
         name='布'
    elif number==3:
         name='蜥蜴'
    elif number==4:
         name='剪刀'
    return name

def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
    """
    comp_number=random.randrange(0,4)
    if player_choice=='石头' or player_choice=='布' or player_choice=='剪刀' or player_choice=='史波克' or player_choice=='蜥蜴':
       print('您的选择为:'+player_choice)
       print('计算机的选择为:'+number_to_name(comp_number))
    else:
        print('“Error: No Correct Name”')
        return
    player_choice_number=name_to_number(player_choice)
    if comp_number==0 and (player_choice_number==3 or player_choice_number==4):
        result=print('机器赢了')
    elif comp_number==1 and (player_choice_number==0 or player_choice_number==4):
        result=print('机器赢了')
    elif comp_number==2 and (player_choice_number==0 or player_choice_number==1):
        result=print('机器赢了')
    elif comp_number==3 and (player_choice_number==2 or player_choice_number==1):
        result=print('机器赢了')
    elif comp_number==4 and (player_choice_number==2 or player_choice_number==3):
        rrsult=print('机器赢了')
    elif comp_number==player_choice_number:
        result=print('您和计算机出的一样呢')
    else:
        result=print('您赢了!')
    return result
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)

