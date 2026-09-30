class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1 = m - 1 
        p2 = n - 1 
        l = m + n - 1 

        while p1 >= 0 and p2 >= 0: 
            if nums1[p1] > nums2[p2]: 
                nums1[p1], nums1[l] = nums1[l], nums1[p1]
                p1 -= 1 
                l -= 1
            else: 
                nums2[p2], nums1[l] = nums1[l], nums2[p2]
                p2 -= 1 
                l -= 1 
        
        nums1[:p2 + 1] = nums2[:p2 + 1]
        

            

