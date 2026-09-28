/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby,
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;
//seccion de inicializacion
int main() {
	int unidades    =0;
	double precio   =0;
	double iva      =0;
	double subtotal =0;
	double pago     =0;
	int n           =0;



	//seccion de entradas
	cout<<"Ingrese la variedad de productos: "<<endl;
	cin>>n;


	//seccion de proceso
	for(int i=1; i<=n; i++) {
		cout<<"Ingrese el precio de su producto : "<< i <<endl;
		cin>>precio;
		cout<<"Ingrese la cantidad de unidades compradas"<<endl;
		cin>>unidades;
		subtotal+=(precio*unidades);
	}

	iva=subtotal*0.19;
	pago=iva+subtotal;

	//seccion de salidas
	cout<<"Su subtotal es:"<<subtotal<<endl;
	cout<<"Su iva es:"<<iva<<endl;
	cout<<"Lo que tiene que pagar es:"<<pago<<endl;

	return 0;
}