class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        vector<int> result(n, 0);
        stack<int> stack;
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && temperatures[stack.top()] < temperatures[i]) {
                int index = stack.top();
                result[index] = i - index;
                stack.pop();
            }

            stack.push(i);
        }

        return result;
    }
};