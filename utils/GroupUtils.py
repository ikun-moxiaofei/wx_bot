# 创建两组字符串
group1 = ["45834099286@chatroom",   # test
          "49102284499@chatroom",   # 1
          "43235807721@chatroom",   # 2
          "49826672161@chatroom",   # 3
          "44020807043@chatroom",   # 4
          "47510776785@chatroom",   # 5
          "43709606838@chatroom",   # 6
          "49050484563@chatroom",   # 7
          "47302088627@chatroom",   # 8
          "50223059128@chatroom",   # 9
          "47310483485@chatroom",   # 10
          "48886574653@chatroom",   # 11
          "50342855327@chatroom",   # 12
          "44452812724@chatroom",   # 13
          "45972093310@chatroom",   # 14
          "48796086668@chatroom",   # 15
          "47310483485@chatroom"    # 16
        ]
group2 = ["test", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "11", "12", "13", "14", "15", "16"]

grouptest = ["45834099286@chatroom"]

def isGroup1(room_wxid):
    if room_wxid in group1:
        print(room_wxid)
        print(getGroupName(room_wxid))
        return 1
    return 0


def isGroupTest(room_wxid):
    if room_wxid in grouptest:
        print(room_wxid)
        print(getGroupName(room_wxid))
        return 1
    return 0


def getGroupName(room_wxid):
    # 使用字典存储一一对应的关系
    mapping = {}
    for i in range(len(group1)):
        mapping[group1[i]] = group2[i]
    return mapping[room_wxid]
