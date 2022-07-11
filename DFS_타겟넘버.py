def solution(numbers, target):
    answer=DFS(0,numbers,target)
    return answer

def DFS(depth,numbers,target):
    answer=0
    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        else: return 0
    else: 
        answer+=DFS(depth+1,numbers,target)
        numbers[depth] *= -1
        answer+=DFS(depth+1,numbers,target)
        #print(answer)
        return answer
    
#solution([1,1,1,1,1],3)