class Solution:
    def threeSum(self, nums):
        sort=sorted(nums)
        x=[]
        for i in range(len(nums)-3):
            value=[nums[i],nums[i+1],nums[i+2]]
            if sum(value)==0:
                if len(list(filter(lambda x:x[0]!=value[0],x)))==0:
                    x.append(value)
        return value
        