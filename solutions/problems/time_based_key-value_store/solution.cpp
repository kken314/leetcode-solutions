class TimeMap {
public:
    unordered_map<string, vector<pair<int, string>>> map; // key -> pair (timestamp, value)
    TimeMap() {
        
    }
    
    void set(string key, string value, int timestamp) {
        map[key].push_back({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        auto& arr = map[key];
        int left = 0;
        int right = arr.size() - 1;
        string res = "";

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (timestamp < arr[mid].first) {
                right = mid - 1;
            } else if (timestamp > arr[mid].first) {
                left = mid + 1;
                res = arr[mid].second;
            } else {
                return arr[mid].second;
            }
        }

        return res;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */