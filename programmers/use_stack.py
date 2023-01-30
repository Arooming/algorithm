# 올바르지 않은 괄호 판단 조건
# 1. string이 끝났는데 stack이 비어있지 않은 경우
# 2. ')'가 들어왔는데 stack이 비어있는 경우

def solution(s):
    stack = []
    
    # 문자열 내부를 돌면서
    for i in s :
    
        # 현재 들어온 문자열이 '('인 경우
        if (i == '(') :
            # stack에 해당 데이터 쌓아주기
            stack.append(i)
            
        # 현재 들어온 문자열이 ')'인 경우
        else :
            # stack이 비어있으면
            if (len(stack) == 0) :
            	# False
                return False
            # stack에 데이터가 있으면    
            else :
            	# 데이터 꺼내기
                stack.pop()
    
    # 문자열 내부를 다 돌았을 때, stack에 남아있는 데이터가 없다면 True 반환
    return len(stack) == 0
