/******************************************************************************

Ejemplos de uso basico de arreglos

*******************************************************************************/
#include <iostream>
using namespace std;

const int TAM=10;
void mostrar(int [],int);
int buscar(int[], int, int);
int main()
{
	// declaracion del arreglo e inicializacion de sus valores
	// int datos[TAM] = {2,6,10,14,18,22,26,30,34,38,42,50};  // error
	int datos[TAM] = {2,6,10,14,18,22,26,30,34,38};

	string palabra;

	// Ingreso de datos de tipo string (un string es un arreglo de caracteres ...)
	cout << "Ingrese su primer nombre: ";
	cin >> palabra;

	// ingreso de algunos datos desde teclado
	/*cout << "Ingreso de algunos datos al arreglo (lugares pares): " << endl;
	for ( int i = 0; i <= TAM-1; i+=2 )
	{
	    cout << "Datos[" << i <<"] = ";
	    cin >> datos[i];
	} */

	// asignacion de un valor en una ubicacion especifica (indice especifico)
	datos [5] = 1000;
	datos [0] = 4000;

	// recorrido por el arreglo para mostrar el contenido de sus elementos
	cout << "Contenidos del arreglo: " << endl;
	for ( int i = 0; i <= TAM; i++ )
	{
		cout << datos[i] << endl;
	}

	// recorrido por el arreglo en orden inverso
	cout << "Contenidos del arreglo: " << endl; //mostrar datos
	mostrar (datos, 10);
	/*for ( int i = TAM-1; i >= 0; i-- )
	{
	    cout << datos[i] << endl;
	}*/
	cout << "Buscar datos del arreglo (valor 30): " << endl;
	int resultado = buscar(datos, 10, 30);
	if (resultado != -1) {
		cout << "El valor fue encontrado en el indice: " << resultado << endl;
	} else {
		cout << "El valor no se encuentra en el arreglo." << endl;
	}
	// mostrar los caracteres de la palabra, en los indices 0 y 3
	cout << "Caracteres de la palabra ingresada..." << endl;
	for ( int i = 0; i <= TAM-1; i++ )
	{
		cout << palabra[i] << endl;
	}

	return 0;
}
void mostrar (int P[], int cant) //primera funcion (mostrar)
{
	for (int i=0; i<cant; i++) {
		cout<<P[i]<<endl;
	}


}

int buscar (int Q[], int cantidad, int valor) //segunda funcion (buscar)
{
	for (int i=0; i<cantidad; i++) {
		if (valor==Q[i]) {
			return i;
		}

	}
	return -1;
}

