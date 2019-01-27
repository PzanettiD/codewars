// Return the sum of all the multiples of 3 or 5 below the number passed in.
// https://www.codewars.com/kata/multiples-of-3-or-5/train/cpp
#include <iostream>
using namespace std;
int solution(int number) 
{
  int sum = 0;
  for (int i = 0; i < number; i++)
  {
    if ((i % 3 == 0) or (i % 5 == 0))
    {
      sum += i;
    }
  }
  return sum;
}


int main()
{
    int outpt = solution(10);
    cout << outpt << endl;
}