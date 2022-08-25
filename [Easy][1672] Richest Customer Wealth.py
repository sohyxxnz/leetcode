# a basic solution with for loop and max function
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for account in accounts:
            curr_customer_wealth = sum(account)
            max_wealth = max(curr_customer_wealth, max_wealth)
        return max_wealth
      
# a solution with map function
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))

# a solution in one line
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(account) for account in accounts])
      
# in comparison with Java
class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxWealth = 0;
        for(int[] account: accounts){
            int currWealth = 0;
            for(int money: account) currWealth += money;
            maxWealth = Math.max(currWealth, maxWealth);
        }

        return maxWealth;
    }
}
