

#include <iostream>
using namespace std;

int fibonacci(int n) {

    if (n <= 1) {
        return 1;
    }
    else{
    
        return (n-1) + (n-2);

    }
    
}


int main(){


// What we know is how to have fibonacci return F(n) = (n-1) * (n-2)
int n;
cout << "";
cin >> n;
cout << fibonacci(n) << endl;
}