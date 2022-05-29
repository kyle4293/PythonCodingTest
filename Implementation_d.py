#게임 개발

n,m=map(int,input().split())
a,b,d=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]
#arr=[],for i in range(n):arr.append(list(map~))
arr[a][b]=2
count=1

amove=[-1,0,+1,0]
bmove=[0,-1,0,+1]
f=0
while(True):
  if f==4:
    na=a-amove[d]
    nb=b-bmove[d]
    if arr[na][nb]==1:
      break
    a,b=na,nb
    continue
    
  if d==0: d=3 #이 과정을 turn_left()라는 함수를 만들어 대신할 수 있다
  else: d-=1 # def turn_left(): d-=1,if d==-1: d=3
  na=a+amove[d]
  nb=b+bmove[d]
  
  if arr[na][nb]!=0:
    f+=1
    continue
  a,b=na,nb
  arr[a][b]=2
  count+=1
  f=0

print(count)
