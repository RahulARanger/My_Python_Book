n=int(input())
nums=[int(i) for i in input().split()]
index_a=nums.index(max(nums))
a=nums[index_a]
del nums[index_a]
index_a=nums.index(max(nums))
b=nums[index_a]
del nums[index_a]
print(a*b)