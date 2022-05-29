#시각

n=int(input())
num=0
while(n>=0):
  if n==3 or n==13 or n==23:
    num+=3600

  else:  
    num+=1575

  n-=1
  
print(num)

#다른 풀이: 매 시각 문자열로 바꾼 다음 문자열 비교
#for i in range(n+1):
#  for j in range(60):
#    for k in range(60):
#      if '3' in str(i)+str(j)+str(k)