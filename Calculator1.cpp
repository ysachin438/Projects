// This code is for calculator
#include<iostream>
using namespace std;
int main(){
char a;
double b, c;
// Taking inputs in the format - a * b
 cout<<"Enter 1st number: ";
 cin>>b;
 cout<<"\nEnter operator: ";
 cin>>a;
 cout<<"\nEnter 2nd number: ";
 cin>>c;
  // logic for calculation and output
switch(a){
   case '+':
   cout<<b<<" "<<a<<" "<<c<<" = "<<(b+c)<<endl;
   break;
   case '-':
   cout<<b<<" "<<a<<" "<<c<<" = "<<(b-c)<<endl;
   break;
   case '*':
   cout<<b<<" "<<a<<" "<<c<<" = "<<(b*c)<<endl;
   break;
   case '/':
   cout<<b<<" "<<a<<" "<<c<<" = "<<(b/c)<<endl;
   break;
}
return 0;
}