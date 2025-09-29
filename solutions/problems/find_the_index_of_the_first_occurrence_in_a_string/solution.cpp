class Solution {
public:
    int strStr(string haystack, string needle) {
        int N = haystack.length();
        int n = needle.length();
        for (int i = 0; i < N-n+1; i++){
            bool all_correct = true;
            for (int j = i; j < i+n;j++){
                if (haystack[j] != needle[j-i]){
                    all_correct = false;
                }
            }
            if (all_correct){
                return i;
            }
        }
        return -1;
    }
};