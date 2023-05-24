#include <iostream>
#include <stack>
using namespace std;

void DecimalToBinary(int decimalNumber) {
    stack<int> binaryStack;

    while (decimalNumber > 0) {
        int remainder = decimalNumber % 2;
        binaryStack.push(remainder);
        decimalNumber /= 2;
    }

    while (!binaryStack.empty()) {
        cout << binaryStack.top();
        binaryStack.pop();
    }
}

int main() {
    int decimalNumber;
    cout << "Ingrese un número decimal: ";
    cin >> decimalNumber;

    cout << "El número binario correspondiente es: ";
    DecimalToBinary(decimalNumber);

    return 0;
}
