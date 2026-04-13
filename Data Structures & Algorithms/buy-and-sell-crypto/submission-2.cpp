#include <iostream>
#include <algorithm>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int minimumPrice = prices[0];
        int buy = 0;

        for (int i = 0; i < std::size(prices); i++) {
            while (buy < i) {
                int currentBuy = prices[buy];
                minimumPrice = std::min(currentBuy, minimumPrice);
                buy++;
            }

            int currentProfit = prices[i] - minimumPrice;

            profit = std::max(currentProfit, profit);
        }
        return profit;
    }
};
