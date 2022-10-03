/*variable types:
1.int----integers
2.float----decimal numbers
3.char----stores any character
4.double----same as float but more precise
5.bool-----true or false

user definded data types:
1.struct
2.union
3.enum

derived data types:
1.array
2.function
3.pointer*/


#include<iostream>
int glo = 11;
using namespace std;
void sum(){
    int a;
    cout<<glo<<" \n";
}
int main(){
    // int a=4;
    // int b=7;
    int glo = 42;
    glo = 342;
    int a=4,b=11;
    double pi = 3.1415926;
    char c= 'k';
    sum();
    cout<<glo;
    // cout<<"This is tutorial 4. \nHere the value of a is "<<a<<". \nThe value of b is "<<b;
    // cout<<"\nThe value of pi is "<<pi;
    // cout<<"\nThe value of character is "<<c;
    return 0;
}