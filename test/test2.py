#coding:utf-8
def sum_add(num):
    sum=0
    for i in range(num+1):
        sum=sum+i
    return sum
def sum_prime(num):
    if num==2:
        sum=2
    elif num>2:
        sum = 2
        for i in range(3,num+1):
            for k in range(2,i):
                if (i%k==0):
                    break
                elif(k==i-1):
                    sum = sum + i
    return sum
print(sum_add(100))
print(sum_prime(2))