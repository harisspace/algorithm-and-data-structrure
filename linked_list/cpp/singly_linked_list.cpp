#include <iostream>

struct Node
{
	Node(int value, Node* node)
	{
		m_Value = value;
		m_Next = node;
	}
	int m_Value;
	Node* m_Next;
};

class SinglyLinkedList
{
public:
	void InsertEnd(int value)
	{
		Node* newNode = new Node(value, nullptr);
		// If head is nullptr
		if (!m_Head)
		{
			m_Head = newNode;
			return;
		}

		Node* current = m_Head;
		while (current)
		{
			if (current->m_Next == nullptr)
			{
				current->m_Next = newNode; break;
			}
			current = current->m_Next;
		}
	}

	void RemoveEnd()
	{
		Node* current = m_Head;
		while (current)
		{
			if (current->m_Next != nullptr && current->m_Next->m_Next == nullptr) break;
			current = current->m_Next;
		}
		delete current->m_Next;
		current->m_Next = nullptr;
	}

	void PrintList()
	{
		Node* current = m_Head;
		while (current)
		{
			std::cout << current->m_Value << "\n";
			current = current->m_Next;
		}
	}
public:
	Node* m_Head = nullptr;
};

int main()
{
	SinglyLinkedList list;
	list.InsertEnd(1);
	list.InsertEnd(2);
	list.InsertEnd(3);
	list.InsertEnd(4);
	list.RemoveEnd();
	list.PrintList();
}