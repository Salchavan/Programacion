#include "header.h"
int main (){
    
    int num = 0;
    cout << "Escriba un numero: ";
    cin >> num;
    cout << "Su tabla de multiplicar es: " << "\n";
    for (int i = 0; i <= 10; i++){
        cout << num << " X " << i << " = " << num * i << "\n";
    }
    cout << "El perimetro del cuadrado seria: " << num * 4 << "\n";
    cout << "El area del cudrado seria: " << num * num << "\n";
    return 0;
};