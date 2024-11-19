#include <iostream>
using namespace std;
long long suma(long long n){
    long long  resultado = 0;
    for (long long i = 0; i < n; i++){
        long long numero = 0, resultado;
        cout << "(" << i + 1 << " de " << n << ")" << " Ingrese el numero a sumar: ";
        cin >> numero;
        long long resultado = resultado + numero;
        cout << resultado << "\n";

    }
    cout << resultado << "\n";
}
int main(){
    long long  n = 0;
    cout << "Ingrese la cantidad de numeros a sumar: ";
    cin >> n;
    suma(n);
};