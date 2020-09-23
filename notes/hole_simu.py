import random

question = [1, 0, 0]

# プレイヤーは必ず一番左(0番目)を選択する
player_select_idx = 0
good_num = 0

def not_chenge():
    global good_num
    # print(question)
    # for idx in range(len(question)):
    #     print(idx)
    #     if question[idx] == 0:
    #         print(question[idx])
    #         break
    # hole_idx = 0
    random.shuffle(question)
    # for idx, val in enumerate(question):
    #     if val == 0:
    #         hole_idx = idx
    #         break
    # print("ホールが開けたのは", hole_idx)
    if question[player_select_idx] == 1:
        good_num += 1
    #     print("○")
    # else:
    #     print("❌")
    
# not_chenge()
def change():
    global good_num
    hole_idx = 0
    # good_index = 0
    random.shuffle(question)
    # for idx, val in enumerate(question):
    #     if val == 1:
    #         # 正解のインデックスを取得
    #         good_idx = idx
    #         break
    # もし最初に選んでいたのが正解だった場合[1,0,0]
    if question[0] == 1:
        hole_idx = random.choice([1,2])
    elif question[1] == 1: # [0,1,0]
        hole_idx = 2
    else: # [0,0,1]
        hole_idx = 1
    # print("ホールが開けたのは", hole_idx)
    if hole_idx == 1:
        player_select_idx = 2
    elif hole_idx == 2:
        player_select_idx = 1
    if question[player_select_idx] == 1:
        good_num += 1
    #     print("○")
    # else:
    #     print("❌")


def simu1(time):
    global good_num
    good_num = 0
    for i in range(time):
        not_chenge()
    # print(good_num)
    good_percent = good_num/time * 100
    # print("100回繰り返して成功した確率は", good_percent)
    return good_percent

def simu2(time):
    global good_num 
    good_num = 0
    for i in range(time):
        change()
    # print(good_num)
    good_percent = good_num/time * 100
    # print("100回繰り返して成功した確率は", good_percent)
    return good_percent

def simu(time):
    per1 = round(simu1(time),2)
    per2 = round(simu2(time),2)
    print("選択を変えなかった時の確率:{0}| 選択を変えたときの確率:{1} *抽出回数{2:,}回".format(per1, per2, time))

simu(100000)