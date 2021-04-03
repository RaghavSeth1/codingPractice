# This is the code to sort the Integer , Input = 56172 , Output = 12567

input = input("Enter your number which you want to sort: ")
res = [int(i) for i in str(input)]
#print(str(res))

for x in range(len(res)):
    for y in range(x+1, len(res)):
        if res[x]>res[y]:
            temp=res[x]
            res[x]=res[y]
            res[y]=temp

print(''.join(map(str,res)))