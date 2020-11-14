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
    tmpsm=sm
    i_one=0
    i_two=0
    for i in range(one+two):
        print(i_one+i_two)
        tmpsm = tmpsm - i_one * 1
        tmpsm = tmpsm - i_two * 2
        if tmpsm%3==0:
            ans=i_one + i_two
        if i_one <= i_two:
            i_one +=1
        else:
            i_two +=1
    if ans == len(N): print("-1")
    else: print(ans)


