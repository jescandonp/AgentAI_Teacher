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
	double descuento=0;



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
	
	//subtotal > 100.000 = Descuento = 10%
	//subtotal > 50.000 && < 100.000 = Descuento = 5%
	//Descuento = 0% 
	
	
if(subtotal>100000){
    cout<<"Tienes un descuento del 10% "<<endl;
    descuento = 0.10;
    
}else if ( (subtotal >= 50000 )  && (subtotal <= 100000 )){
    cout<<"Tienes un descuento del 5% "<<endl;
    descuento = 0.05;
    
}
else{
    cout<<"No tienes descuento "<<endl;
    descuento = 0.0;
}



	//seccion de salidas
	subtotal = subtotal - (subtotal*descuento);
	iva= subtotal*0.19;
	pago=subtotal+iva;
	cout<<"Su subtotal es:"<<subtotal<<endl;
	cout<<"Su iva es:"<<iva<<endl;
	cout<<"Lo que tiene que pagar es:"<<pago<<endl;
	

	return 0;
}