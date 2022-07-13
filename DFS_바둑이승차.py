'''
바둑이 승차
C킬로 그램 넘게 태울 수 없음.
C를 넘지 않으면서 바둑이들을 가장 무겁게 태우기
N마리 바둑이 W바둑이 무게
가장 무거운 무게 구하기

입력예제 C N
'''


def DFS(L,sum):
    global result
    
    if sum > c:
        return 
    
    if L==n: # 말단 노드에 왔다
        if sum > result :
            result=sum
        
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)
        
    
if __name__ == "__main__":
 
    c,n=map(int,input().split())
    a=[]
    result=-2147000000
    for i in range(n):
        d=int(input())
        a.append(d)
   # print(a)
        #a[i]=int(input())
        
    DFS(0,0)
    print(result)