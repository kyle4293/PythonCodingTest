#상하좌우

n=int(input())
plan=input().split()
x, y = 1, 1
move=['R','L','U','D']
xmove=[0,0,-1,1]
ymove=[1,-1,0,0]
for i in plan:
  nx=x+xmove[move.index(i)]
  ny=y+ymove[move.index(i)]

  if nx<1 or ny<1 or nx>n or ny>n:
    continue

  x,y = nx, ny
  
print(x,y)