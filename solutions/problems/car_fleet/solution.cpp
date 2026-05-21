class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int, int>> cars;

        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }

        sort(cars.rbegin(), cars.rend());

        vector<double> car_fleet;
        for (auto car : cars) {
            double pos = car.first;
            double v = car.second;
            car_fleet.push_back((target - pos) / v);
            if (car_fleet.size() >= 2 && car_fleet[car_fleet.size() - 2] >= car_fleet.back()) {
                car_fleet.pop_back();
            }
        }

        return car_fleet.size();
    }
};