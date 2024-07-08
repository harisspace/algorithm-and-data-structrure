#include <iostream>
#include <vector>

class Stack
{
public:
	void Push(int value)
	{
		m_Container.push_back(value);
	}
	void Pop()
	{
		if (m_Container.size() < 1) return;
		m_Container.pop_back();
	}
	int Peek()
	{
		return m_Container.at(m_Container.size() - 1);
	}
	void Print()
	{
		for (int& v : m_Container)
		{
			std::cout << v << "\n";
		}
	}
private:
	std::vector<int> m_Container;
};

int main()
{
	Stack stack;
	stack.Push(1);
	stack.Push(2);
	stack.Push(3);
	stack.Pop();
	int lastValue = stack.Peek();
	std::cout << "Lastvalue: " << lastValue << "\n";
	stack.Print();

	std::cin.get();
}