// Calculatin one's compliment of binary number using class in c++
#include <iostream>
#include <string>
using namespace std;
class binary
{
    string s;

public:
    void read(void);
    void chk_bin(void);
    void ones(void);
    void display(void);
};
// input a binary number
void binary ::read(void)
{
    cout << "Enter a binary number" << endl;
    cin >> s;
}
// check binary format
void binary ::chk_bin(void)
{
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) != '0' && s.at(i) != '1')
        {
            cout << "Invalid binary format." << endl;
            exit(0);
        }
    }
}
// convert 1--> '0' & 0 --> '1'
void binary ::ones(void)
{
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) == '0')
        {
            s.at(i) = '1';
        }
        else
        {
            s.at(i) = '0';
        }
    }
    cout<<"1's compliment is: "<<s<<endl;
}
// checking for palindrome
void binary ::display(void)
{
    int m = s.length();
    for (int i = 0; i < s.length(); i++)
    {
        if (s.at(i) != s.at(m-i-1))
        {
            cout << "No, it is not a palindrome" << endl;
            exit(0);
        }
    }
    cout << "Yes, it is a palindrome." << endl;
}
int main()
{
    binary b;
    b.read();
    b.chk_bin();
    b.ones();
    b.display();

    return 0;
}