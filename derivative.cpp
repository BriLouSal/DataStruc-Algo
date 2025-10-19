

#include <iostream>
#include <vector>
using namespace std;


int derivative(int a, int n){

    if (n == 0){
        return 0;
    }
    else{
        // We want to do is for example 3x^2 = (2)(3) * x^(2-1)
        return (a * n), n - 1;
    }

    return 0;
    
    
}



int main(){
    int a, n;


    cout << "";
    cin >> a, n;


    derivative(a, n);

    return 0;
}
// Let a = coefficent, and n = power