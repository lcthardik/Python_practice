nums=[1,2,2,2,3,3,4,4,4,5,6,7,8,8,8]

i=0
j=1
flag=False

while(j<len(nums)):
    if (nums[i]!=nums[j]):
        i+=1
        j+=1
        flag=False
    elif (nums[i]==nums[j] and flag):
        nums.pop(j)
    else:
        i+=1
        j+=1
        flag=True

print(nums)