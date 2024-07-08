#include <iostream>

int Factorial(int number)
{
	if (number <= 1)
	{
		return number;
	}

	return number * Factorial(number - 1);
}

int main()
{
	int result = Factorial(5);
	std::cout << result;
}