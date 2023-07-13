class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        point1,point2=0,0
        result=[]
        while point1<len(nums1) and point2<len(nums2):
            if nums1[point1]<=nums2[point2]:
                result.append(nums1[point1])
                nums1.pop(point1)
            elif nums1[point1]>=nums2[point2]:
                result.append(nums2[point2])
                nums2.pop(point2)
        if len(nums1)>0:
            result.extend(nums1)
        if len(nums2)>0:
            result.extend(nums2)
        print(nums1,nums2)
        if len(result)%2!=0:
           return result[int(len(result)/2)]
        else:
           mid=int(len(result)/2)
           return (result[mid]+result[mid-1])/2