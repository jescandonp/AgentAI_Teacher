/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby,
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
using namespace std;
//seccion de entradas
int main() {
int unidades;
double precio;
double iva;
double subtotal;
double pago;


//seccion de entradas
cout<<"Ingrese el precio de su producto"<<endl;
cin>>precio;
cout<<"Ingrese la cantidad de unidades compradas"<<endl;
cin>>unidades;

//seccion de proceso
subtotal=precio*unidades;
iva=subtotal*0.19;
pago=iva+subtotal;
 
 //seccion de salidas
 cout<<"Su subtotal es:"<<subtotal<<endl;
 cout<<"Su iva es:"<<iva<<endl;
 cout<<"Lo que tiene que pagar es:"<<pago<<endl;

	return 0;
}