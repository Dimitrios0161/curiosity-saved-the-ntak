/* #include <iostream>
#define LIMIT (1000-1)

int main()
{
	int sum = 0;
	sum += 3 * (LIMIT/3+1) * (LIMIT/3) / 2;
	sum += 5 * (LIMIT/5+1) * (LIMIT/5) / 2;
	sum -= 15 * (LIMIT/15+1) * (LIMIT/15) / 2;
	std::cout << sum << "\n";
} */


#include <iostream>

// triangular number: `sum{x}=1+2+..+x = x*(x+1)/2`
unsigned long long sum(unsigned long long x)
{
  return x * (x + 1) / 2;
}

int main()
{
  unsigned int tests;
  std::cin >> tests;
  while (tests--)
  {
    unsigned long long last;
    std::cin >> last;

    // not including that number
    last--;

    // find sum of all numbers divisible by 3 or 5
    auto sumThree   =  3 * sum(last /  3);
    auto sumFive    =  5 * sum(last /  5);

    // however, those numbers divisible by 3 AND 5 will be counted twice
    auto sumFifteen = 15 * sum(last / 15);

    std::cout << (sumThree + sumFive - sumFifteen) << std::endl;
  }

  return 0;
}