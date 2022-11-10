// Noah Hanshaw, Skylar Schmidt, David Rodriguez
// 11/12/2021
// CISC 3321 Group Project

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Calculator {
public: Calculator(int A, int B, int C) {
    a = A;  // First input number
    b = B;  // Second input number
    result = C;  // Final Output
}
public:
    int addition() {
        result = a + b;
        return result;
    }
    int subtraction() {
        result = a - b;
        return result;
    }
    int multiplication() {
        result = a * b;
        return result;
    }
    double division() {
        result = a / b;
        return result;
    }
public:
    int a;
    int b;
private:
    int result;
};

class secretnumbers : Calculator {

};

int main()
{
    int A{ 0 };
    int B{ 0 };
    int C{ 0 };
    string function;
    
    cout << "Please input your first number" << endl;
    cin >> A;
    cout << "Please input your first number" << endl;
    cin >> B;
    cout << "What function would you like to perform? (Please input one of +,-,*,/)" << endl;
    cin >> function;

    Calculator calc(A, B, C);

    if (function == "+") {
        cout << "Total = " << calc.addition() << endl;
    }
    else if (function == "-") {
        cout << "Difference = " << calc.subtraction() << endl;
    }
    else if (function == "*") {
        cout << "Product = " << calc.multiplication() << endl;
    }
    else if (function == "/") {
        cout << "Quotient = " << calc.division() << endl;
    }

    return 0;
}
