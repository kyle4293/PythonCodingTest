#왕실의 나이트

l=input()

x=ord(l[0])-96
y=int(l[1])

num=0

dx=[2,2,1,1,-2,-2,-1,-1]
dy=[1,-1,2,-2,1,-1,2,-2]

for i in range(8):
  nx=x+dx[i]
  ny=y+dy[i]
  if nx>8 or nx<1 or ny>8 or ny<1:
    continue
  num+=1

print(num)

# 다른 풀이: Dictionary 이용
# steps=[(-2,-1),(-1,-2)...]
# for step in steps:
# x+step[0]//y+step[1]