N = input()
numList = list(N)
one = 0
two = 0
sm = 0
for num in numList:
    if int(num)%3==1: one += 1
    if int(num)%3==2: two += 1
    sm += int(num)
print("one: {}, two: {}, sum:{}".format(one,two,sm))
if one>2: one =2
if two>2: two=2
print("one: {}, two: {}, sum:{}".format(one,two,sm))
ans = -1
if sm%3==0: print("0")
else:
    tmpsm = sm
    for i in range(one):
       tmpsm -=1
       if tmpsm%3==0: 
           ans=i+1
    tmpsm = sm
    for j in range(two):
        tmpsm -=2
        if tmpsm%3==0 and ans==-1 or tmpsm%3==0 and ans>j+1: 
            ans=j+1
    print("-1") if len(N)==ans else print(ans)