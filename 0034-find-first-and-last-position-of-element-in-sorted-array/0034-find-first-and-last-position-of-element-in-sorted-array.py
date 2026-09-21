class Solution:
    def searchRange(self,n:list[int],t:int)->list[int]:
        left,right=0,len(n)-1
        while left<=right:
            mid=(left+right)//2
            if n[mid]>=t:
                right=mid-1
            else:
                left=mid+1
        if left<len(n) and n[left]==t:
            start=left
        else:
            return [-1,-1]
        right=len(n)-1
        while left<=right:
            mid=(left+right)//2
            if n[mid]<=t:
                left=mid+1
            else:
                right=mid-1
        return [start,right]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna