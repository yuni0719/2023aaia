class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #先把數字排好
        ans = [ [ nums[0] ] ] # 把最前面、最小的數字，放在兩層方括號裡
        repeat = 0
        N = len(nums) #有幾個數字
        for i in range(1, N): #想比較 nums[i] vs. nums[i-1] 是否相同
            if nums[i] == nums[i-1]: #這裡要處理，相同，就repeat += 1
                repeat += 1
                if len(ans)<=repeat: # 目前的層數不夠多
                    ans.append( [] ) # 增加一層樓
            else: # 沒有重複
                repeat = 0
            ans[repeat].append( nums[i] )
        return ans