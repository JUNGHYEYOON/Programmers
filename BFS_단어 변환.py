'''
최단거리:BFS,다익스트라
'''

from collections import deque

def solution(begin,target,words):
    answer=0
    q=deque()
    q.append([begin,0])
    #print(q)
    V= [0 for i in range(len(words))]
    
    #print(q)
    while q:
        word,cnt=q.popleft() 
        #print(word,cnt)
        #print(len(words)) -> 6
        #popleft -> 왼쪽에서 값을 빼고 싶은 경우
        #pop -> 오른쪽에서 값을 빼고 싶은 경우
        if word == target:
            answer=cnt
            break
        
        for i in range(len(words)):
            temp_cnt=0
            # print("V[i]",V[i])
            if not V[i]:
                for j in range(len(word)):
                    #print(word[j],words[i][j])
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i],cnt+1])
                    V[i] = 1
    #print(answer)
    return answer               
solution("hit","cog",["hot","dot","dog","lot","log","cog"])
