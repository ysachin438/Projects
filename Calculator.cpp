#include<iostream>
using namespace std;
Sum( int a, int b){
    int c;
c = a+b;
return c;
}
product(int a, int b){
    int c;
    c = a*b;
    return c;
}
divide(int a, int b){
     float c;
    c=a/b;
    return c;
}
subs(int a, int b){
   long c;
   c=a-b;
   return c; 
}
per(int a, int b){
    long c, d;

    c =((a*100)/b);
    return c;
}
square(int a, int b){
    long c;
    c=a*a;
    return c;
}
int main(){
int a, b;
int c;
cout<<"Enter two no."<<endl;
cin>>a>>b;


cout<<"Choose Operator: 1--> Sum,  2--> Product, 3 --> Divide   4--> Substract, 5--> Square, 6-->percentage "<<endl;
cin>>c;
if(c ==1){
cout<<Sum(a,b)<<endl;
}
if(c==2){
    cout<<product(a,b)<<endl;
}
if((c==3)&& (a>b)){
    cout<<divide(a,b)<<endl;
}
for(int i=1; i<=1; i++){
    if((c==4)&&(a>b)){
    cout<<subs(a,b)<<endl;
    }
}
if(c==5){
    cout<<square(a,b)<<endl;
}
if(c==6){
    cout<<per(a,b)<<endl;
}

return 0;
}