class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0 #用來放答案的變數

        N = len(nums) #nums 這個陣列 list 有幾個數
        for i in range(N): 
            for j in range( i+1, N):
                ans = max( ans, (nums[i]-1)*(nums[j]-1) )

        return ans