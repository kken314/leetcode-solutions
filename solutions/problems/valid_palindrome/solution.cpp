class Solution {
public:
    bool isPalindrome(string s) {
        int p1 = 0;
        int p2 = s.length() - 1;
        while (p2 > p1) {
            if (!isalnum(s[p1])) {
                p1++;
                continue;
            }

            if (!isalnum(s[p2])) {
                p2--;
                continue;
            }

            //cout << "p1 : " << s[p1]  << "      p2 : " << s[p2] << endl;

            if (tolower(s[p1]) != tolower(s[p2])) {
                return false;
            }
            p1++;
            p2--;
        }

        return true;
    }
};