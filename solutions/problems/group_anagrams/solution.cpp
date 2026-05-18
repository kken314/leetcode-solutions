class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;

        for (const auto& str : strs) {
            string count(26, 0);

            for (char c : str) {
                count[c - 'a'] += 1;
            }

            groups[count].push_back(str);
        }
        vector<vector<string>> result;

        for (auto& pair : groups) {
            result.push_back(pair.second);
        }

        return result;
    }
};