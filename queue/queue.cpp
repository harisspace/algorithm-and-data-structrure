#include <iostream>

class Node
{
public:
	Node(int value)
		: m_Value(value) {}
public:
	int m_Value;
	Node* m_Next = nullptr;
};

class Queue
{
public:
	void Enqueue(int value)
	{
		Node* newNode = new Node(value);

		if (!left)
		{
			left = newNode;
			right = newNode;
			return;
		}

		newNode->m_Next = left;
		left = newNode;
	}
	void Dequeue()
	{
		if (!left) return;
		Node* tempNode = left;
		left = left->m_Next;
		delete tempNode;
	}
	void Print()
	{
		Node* current = left;
		while (current)
		{
			std::cout << current->m_Value << "\n";
			current = current->m_Next;
		}
	}
private:
	Node* left = nullptr;
	Node* right = nullptr;
};

int main()
{
	Queue queue;
	queue.Enqueue(1);
	queue.Enqueue(2);
	queue.Enqueue(3);
	queue.Dequeue();
	queue.Print();
}