second  = int(input("what's your coutdown time "))
for i in range(0,second):
    print(f"coutdown:{second-i}")
    
N = int(input("what's  the upper limit "))
total = 0
for x in range(1,N+1):
    if x % 3 == 0:
        total += x
    
print(f"计算范围为1到{x}，累加总量为{total}")    
    