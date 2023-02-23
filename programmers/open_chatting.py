# 변경 불가능한 내용: userId (key)
# 변경 가능한 내용: nickName (value)

def solution(record):
    answer = []
    nick = {}
    msg = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for i in record :
        i = i.split()
        # if len(i) == 3
        if i[0] == "Enter" or i[0] == "Change":
            nick[i[1]] = i[2]
    
    for i in record :
        i = i.split()
        if i[0] == "Change" :
            continue
        answer.append(nick[i[1]] + msg[i[0]])

    return answer