num = int(input("請輸入一個數字："))
for i in range(1,num+1):
    for j in range(1,num+1):
        print("%d*%d = %d"%(i,j,i*j), end = " ")
    print()
        