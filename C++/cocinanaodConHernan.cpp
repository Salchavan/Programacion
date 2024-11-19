#include <iostream>
using namespace std;
int main(){
    int nuevaTemperatura = 0, temperaturaMaxima = 0;
    cout << "Ingrese la temperatura maxima del horno: ";
    cin >> temperaturaMaxima;
    while (temperaturaMaxima > 0){
        cout << "Ingrese la nueva temperatura: ";
        cin >> nuevaTemperatura; 
        if (nuevaTemperatura > temperaturaMaxima){
            cout << "TEMPERATURA MUY ALTA!!! WIUWIUWIUWIUWIU";
            break;
        }      
    }

    return 0;
};
