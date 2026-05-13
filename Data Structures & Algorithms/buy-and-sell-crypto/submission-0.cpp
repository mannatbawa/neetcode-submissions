class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = 0;
        int sell = 1;
        int max_profit = 0;
     
        while (sell < prices.size()){
            if (prices[buy] < prices[sell]){
                max_profit = max(max_profit, prices[sell]-prices[buy]);
            }
            else{
                buy = sell;
            }
            sell++;
        }
        return max_profit;
    }
};
