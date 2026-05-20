class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> map = { 
                                            {')', '('},
                                            {']', '['},
                                            {'}', '{'}
                                        };
        stack<char> stack;

        for (char c : s) {
            if (map.count(c)) {
                if (!stack.empty() && map[c] == stack.top()) {
                    stack.pop();
                } else {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }

        return stack.empty();
    }
};