# Action 1：求2+4+6+8+...+100的求和
#function 1
sum=0
for i in range(2,102,2):
    sum=sum+i
print(sum)

#function 2
sum=0
j=0
while(j<=100):
    sum=sum+j
    j=j+2
print(sum)

#function 3
sum=0
def Add(n,m,k):
    temp=0
    for i in range (n,m+k,k):
        temp=temp+i
    return temp
sum=Add(2,100,2)
print (sum)

    
    