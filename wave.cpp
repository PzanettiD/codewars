// Given a string, return an array with one of the characters uppercased. 
// https://www.codewars.com/kata/mexican-wave/train/cpp
#include <iostream>
#include <string>
#include <vector>
#include <locale>
using namespace std;
vector<string> wave(string y){
    vector<string> arrayF;
    string input = y;
    for (int i = 0; i < y.length(); i++)
    {
        string k = y;
        if (isalpha(y[i]))
        {
            k[i] = toupper(y[i]);
            arrayF.push_back(k);
        }
    }
    return arrayF;
}

int main()
{
    vector<string> x = wave("hello");
    vector<string>::iterator it;
    for (it = x.begin(); it != x.end(); it++)
    {
        cout << *it << endl;
    } 
    return 0;
}