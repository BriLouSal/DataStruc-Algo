class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <=  0) {
            return false;
        }
        while (n % 3 == 0){ 
            n = std::floor(n / 3);
        }
        return n == true;
    }
};