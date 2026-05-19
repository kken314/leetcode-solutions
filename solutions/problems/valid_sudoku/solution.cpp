class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //cheak rows
        for (int row = 0; row < 9; row++) {
            unordered_set<char> seen;
            for (int col = 0; col < 9; col++) {
                if(board[row][col] == '.') {
                    continue;
                }

                if (seen.find(board[row][col]) != seen.end()) {
                    return false;
                } else {
                    seen.insert(board[row][col]);
                }
            }
        }

        //cheak columns
        for (int col = 0; col < 9; col++) {
            unordered_set<char> seen;
            for (int row = 0; row < 9; row++) {
                if(board[row][col] == '.') {
                    continue;
                }

                if (seen.find(board[row][col]) != seen.end()) {
                    return false;
                } else {
                    seen.insert(board[row][col]);
                }
            }
        }

        //cheak 3 x 3 boxs
        for (int row_box = 0; row_box < 3; row_box++) {
            for (int col_box = 0; col_box < 3; col_box++) {
                unordered_set<char> seen;
                int top_row = row_box * 3;
                int left_col = col_box * 3;
                for (int row = top_row; row < top_row + 3; row++) {
                    for (int col = left_col; col < left_col + 3; col++) {
                        if(board[row][col] == '.') {
                            continue;
                        }

                        if (seen.find(board[row][col]) != seen.end()) {
                            return false;
                        } else {
                            seen.insert(board[row][col]);
                        }
                    }
                }
            }
        }
        return true;
    }
};