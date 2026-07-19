class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        vector<int> count(26, 0);
        vector<int> curr_count(26, 0);

        for (char c : s1) {
            count[c - 'a']++;
        }

        int left = 0;

        for (int right = 0; right < s2.size(); right++) {
            curr_count[s2[right] - 'a']++;

            if (right - left + 1 > s1.size()) {
                curr_count[s2[left] - 'a']--;
                left++;
            }

            if (right - left + 1 == s1.size()) {
                if (count == curr_count) {
                    return true;
                }
            }
        }

        return false;

    }
};