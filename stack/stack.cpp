#include <iostream>
#include <vector>

int main()
{
	std::vector<int> stack;
	stack.push_back(1);
	stack.push_back(2);
	stack.push_back(3);

	stack.pop_back();

	stack.push_back(4);

	for (int& i : stack)
		std::cout << i << "\n";

	std::cin.get();
}