class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int prev_min = prices[0];
        
        for (int i = 1; i < prices.size(); i++) {
            max_profit = max(max_profit, prices[i] - prev_min);
            prev_min = min(prev_min, prices[i]);
        }

        return max_profit;
    }
};