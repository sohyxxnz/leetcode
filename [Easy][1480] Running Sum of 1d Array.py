# a basic solution with for loop
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums

# a solution with itertools.acuumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

# a solution with slicing
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))] 

# In comparison with Java
class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        ans[0] = nums[0];
        for(int i=1; i<nums.length; i++){
            ans[i] = ans[i-1]+nums[i];
        }
        return ans;
    }
}
