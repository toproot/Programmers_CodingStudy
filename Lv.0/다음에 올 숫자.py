# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

def solution(common):
    answer = 0
    firstMinusNum = 0
    secondMinusNum = 0
    commonMinusNum = 0
    
    for i in range(2):
        if i == 0:
            firstMinusNum = common[i+1] - common[i]
        elif i == 1:
            secondMinusNum = common[i+1] - common[i]
    
    if firstMinusNum == secondMinusNum:
        commonMinusNum = firstMinusNum
        answer = common[-1] + commonMinusNum
    else:
        commonMinusNum = secondMinusNum / firstMinusNum
        answer = common[-1] * commonMinusNum
    
    return answer
