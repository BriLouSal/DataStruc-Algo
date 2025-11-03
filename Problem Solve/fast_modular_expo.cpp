
#include <iostream>
#include <vector>
using namespace std;


// Key Observation:

//  a^m 


int fastfast(long long n, int a, int MOD){
    int answers = 1;

    while (n >= 1){
        if (n % 2 == 0){
        a = (a * a) % MOD;
        n/2;

        }
        else{
            a = (a * a) % MOD;
            n--;
        }

    }



    return a;
}



int main(){




    


    cout << fastfast(7, 0, 1000000001);
    // m = a * b,
    //  b = a/b therefore, a >= b, else if not a * b > a ** 2



    return 0;
}