// Noah Hanshaw, Skylar Schmidt, David Rodriguez
// 11/12/2021
// CISC 3321 Group Project

#include <iostream>
#include <string>
#include <sstream>
using namespace std;

class Values {
public: Values(float A, float B) {
    a = A;
    b = B;
    cout << "Enter your first number: ";
    cin >> a;
    cout << "Enter your second number: ";
    cin >> b;
}
public:
      float a;
      float b;
};

class Addition : public Values {
public:
    Addition(float a, float b, float c) : Values(a,b) {
        result = c;
    }
    float add() {
        result = a + b;
        cout << "Total = " << result << endl;
        return result;
    }
private:
    float result;
};

class Subtraction : public Values {
public:
    Subtraction(float a, float b, float c) : Values(a, b) {
        result = c;
    }
    float subtract() {
        result = a - b;
        cout << "Difference = " << result << endl;
        return result;
    }
private:
    float result;
};

class Multiplication : public Values {
public:
    Multiplication(float a, float b, float c) : Values(a, b) {
        result = c;
    }
    float multiply() {
        result = a * b;
        cout << "Product = " << result << endl;
        return result;
    }
private:
    float result;
};

class Division : public Values {
public:
    Division(float a, float b, float c) : Values(a, b) {
        result = c;
    }
    float divide() {
        result = a / b;
        cout << "Quotient = " << result << endl;
        return result;
    }
private:
    float result;
};

int main()
{
    float a{ 0 };
    float b{ 0 };
    float c{ 0 };
    string function;

    cout << "Choose a function (+,-,*,/)" << endl;
    cin >> function;

    if (function == "+") {
        Addition Add(a, b, c);
        Add.add();
    }
    else if (function == "-") {
        Subtraction Subtract(a, b, c);
        Subtract.subtract();
    }
    else if (function == "*") {
        Multiplication Multiply(a, b, c);
        Multiply.multiply();
    }
    else if (function == "/") {
        Division Divide(a, b, c);
        Divide.divide();
    }
    else {
        cout << "ERROR: Incorrect function input. Please try again";
    }
    return 0;
}