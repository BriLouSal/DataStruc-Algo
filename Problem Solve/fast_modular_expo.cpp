
#include <iostream>
#include <vector>
using namespace std;


// Time Complexity: O(log(n))

int fastfast(long long n, int a, int MOD){
    long long result = 1;
    long long base = a % MOD;


    while (n >= 1){
        if (n % 2 == 0){
        result = (result * base) % MOD;
        n/2;

        }
        else{
            base = (base * base) % MOD;
            n--;
        }

    }



    return result;
}



int main(){




    


    cout << fastfast(7, 0, 1000000001);
    // m = a * b,
    //  b = a/b therefore, a >= b, else if not a * b > a ** 2



    return 0;
}