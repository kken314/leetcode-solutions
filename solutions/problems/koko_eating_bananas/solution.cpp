class Solution {
public:
    bool valid(int k, vector<int>& piles, int h) {
        if (k <= 0) {
            return false;
        }

        int time = 0;
        for (int i = 0; i < piles.size(); i++) {
            time += (piles[i] + k - 1) / k;
            // time += piles[i] / k
            // if (piles[i] % k) {
            //     time++;
            // }
        }
        return time <= h;
    }

    int minEatingSpeed(vector<int>& piles, int h) {

        int max_pile = 0;

        for (int i = 0; i < piles.size(); i++) {
            max_pile = max(piles[i], max_pile);
        }

        int right = max_pile; 
        int left = 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            cout << "left : " << left << " mid : " << mid << " right : " << right << endl;
            if (valid(mid, piles, h)) {
                if (valid(mid - 1, piles, h)) {
                    right = mid - 1;
                } else {
                    return mid;
                }
            } else {
                left = mid + 1;
            }
        }
    
        return -1;
    }
};