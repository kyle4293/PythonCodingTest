#숫자 카드 게임

n,m=map(int,input().split())

data=[]
for i in range(n):
  num=list(map(int,input().split()))
  data.append(min(num))
print(max(data))