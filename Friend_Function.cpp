// Friend Function In class--
/*
#include<iostream>
using namespace std;

class complex{
    int a,b;
    public:
    void setnumber(int n1, int n2){
        a = n1;
        b= n2;
    }
    friend complex sumcomplex(complex o1, complex o2);
    void printnumber(){
        std::cout<<a<<" + "<<b<<"i"<<endl;
    }
};
complex sumcomplex(complex o1, complex o2){
    complex o3;
    o3.setnumber((o1.a + o2.a), (o1.b+o2.b));
    return o3;
}
int main(){
    complex c1,c2,c3;
    c1.setnumber(1,2);
    c1.printnumber();

    c2.setnumber(4,5);
    c2.printnumber();

    complex sum;
    sum = sumcomplex(c1,c2);
    sum.printnumber();

return 0;
}
*/

/*
#include <iostream>
using namespace std;
// Forward Declartion
class complex;

class calculator
{
public:
    int add(int a, int b)
    {
        return (a + b);
    }
    int sumrealcomplex(complex, complex);
    int sumcompcomplex(complex, complex);
};

class complex
{
    int a, b;
    // Individually declaring as friends
    // friend int calculator ::sumrealcomplex(complex, complex);
    // friend int calculator ::sumcompcomplex(complex, complex);

    // alter : Declaring the entire calculator class as friend
    friend class calculator;

public:
    void setnumber(int n1, int n2)
    {
        a = n1;
        b = n2;
    }
};

int calculator ::sumrealcomplex(complex o1, complex o2)
{
    return (o1.a + o2.a);
}

int calculator ::sumcompcomplex(complex o1, complex o2)
{
    return (o1.b + o2.b);
}

int main()
{
    complex o1, o2;
    o1.setnumber(1, 4);
    o2.setnumber(5, 7);

    calculator c1;

    int result = c1.sumrealcomplex(o1, o2);
    cout << "the sum of real part is " << result << endl;

    int result2 = c1.sumcompcomplex(o1, o2);
    cout << "the sum of complex part is " << result2 << endl;
    return 0;
}

*/

/*
#include<iostream>
using namespace std;
class Y;
class X{
    int data;
    public:
    void setavalue(int value){
        data = value;
    }
    friend void add(X,Y);
};
class Y{
    int num;
    friend void add(X,Y);
    public:
    void setvalue(int value){
        num = value;
    }
};
void add(X o1, Y o2){
    cout<<"Summing data of X and Y objects given me "<<o1.data + o2.num<<endl;

}
int main(){
    X a1;
    a1.setavalue(3);

    Y a2;
    a2.setvalue(15);
    add(a1,a2);


return 0;
}

*/

// Exchanging object values of different class;
#include <iostream>
using namespace std;
class c2;

class c1
{
    friend void exchange(c1 &, c2 &);
    int val1;

public:
    void setvalue(int data)
    {
        val1 = data;
    }
    void display()
    {
        cout << "The value of val1 is" << val1 << endl;
    }
};
class c2
{
    int val2;
    friend void exchange(c1 &, c2 &);

public:
    void setvalue(int data)
    {
        val2 = data;
    }
    void display()
    {
        cout << "The value of val1 is " << val2 << endl;
    }
};
void exchange(c1 &x, c2 &y)
{
    int temp = y.val2;
    y.val2 = x.val1;
    x.val1 = temp;
}
int main()
{
    c1 a1;
    c2 a2;
    a1.setvalue(3);
    a2.setvalue(5);
    
    exchange(a1, a2);

    cout << "Values after exchanging:" << endl;
    a1.display();
    a2.display();
}