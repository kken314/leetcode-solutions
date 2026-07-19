class Solution {
public:
    int characterReplacement(string s, int k) {
        int left = 0;
        int right = 0;
        int count[26] = {0};
        int max_valid_substring = 0;

        for (right = 0; right < s.size(); right++) {
            count[s[right] - 'A']++;
            
            int curr_max = 0;
            for (int num : count) {
                curr_max = max(curr_max, num);
            }

            while ((right - left + 1) - curr_max > k) {
                count[s[left] - 'A']--;
                left++;
            }

            max_valid_substring = max(max_valid_substring, right - left + 1);
        }

        return max_valid_substring;
    }
};