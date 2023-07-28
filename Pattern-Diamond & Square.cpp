// Printing patterns - Diamond and Square--
#include<iostream>
using namespace std;
int main(){
    int i,k,j,n;
    cout<<"Enter a number : ";
    cin>>n;
    // Printing Diamond shape---
    cout<<"Diamond"<<endl;
    for(i=0;i<n;i++){
        for(j=n;j>i;j--){
            cout<<" ";
        }
        for(k=0;k<=i;k++){
            cout<<"* ";
        }
        cout<<endl;
        
    }
    for(i=0;i<n;i++){
        for(j=0;j<i+2;j++){
            cout<<" ";

        }
        for(k=n-1;k>i;k--){
            cout<<"* ";

        }
        cout<<endl;
    }


    //Sqaure
    cout<<"\nSqaure\n";
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(i==0||i==n-1){
                cout<<"* ";
            }
            else if(j==0||j==n-1){
                cout<<"* ";
            }
            else{
                cout<<"  ";
            }
            
        }
        cout<<endl;
    }

return 0;
}