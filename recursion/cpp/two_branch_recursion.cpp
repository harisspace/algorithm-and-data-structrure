#include <iostream>

int Fibonacci(int number)
{
	if (number <= 1)
	{
		return number;
	}

	return Fibonacci(number - 1) + Fibonacci(number - 2);
}

int main()
{
	int result = Fibonacci(5);
	std::cout << result;
}