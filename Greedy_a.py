#큰 수의 법칙
n,m,k=map(int,input().split())
data=list(map(int,input().split()))

data.sort(reverse=True)
num=0
while(m>0):
  for j in range(k):
    num+=data[0]
    m-=1
  num+=data[1]
  m-=1

print(num)