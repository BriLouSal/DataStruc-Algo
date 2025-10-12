
#include <iostream>
#include <vector>
using namespace std;

int prime(int a){

    if (a % 2 == 0){
        return false;
    }
    if (a == 2) {
        return true;
    }
    else if (a == 1) {
        return false;
    }

    for (int i = 2; i * i < a; ++i) {
         

        // Since we know most non-prime number is divisble 2, we can let it = fALSE IF CONDITION IS MET, HOWEVER CONSIDER DIVISBILITY BY 3, ETC. so CONSIDER I * I

        if (a % i == 0) {
            return false;

        }
    }
    return true;
}


int main(){


    int a;

    cout << "";
    cin >> a;

    // m = a * b,
    //  b = a/b therefore, a >= b, else if not a * b > a ** 2







    
    return 0;
}