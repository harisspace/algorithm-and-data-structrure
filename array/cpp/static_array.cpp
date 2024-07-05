#include <iostream>
#include <string>

template <unsigned int T>
class StaticArray
{
public:
	StaticArray()
	{
		for (int i = 0; i < m_Capacity; i++)
		{
			m_Array[i] = 0;
		}
	}

	inline unsigned int Length() { return m_Length; };

	void Print()
	{
		std::cout << "Size: " << m_Length << std::endl;
		for (int i = 0; i < m_Length; i++)
		{
			std::cout << "Array" << i << ": " << m_Array[i] << std::endl;
		}
	}

	// Add value at the end of the array
	// O(1)
	int Append(int value)
	{
		if (m_Length >= m_Capacity)
			return -1;
		m_Array[m_Length] = value;
		m_Length += 1;
		return 1;
	}

	// Add value at the beginning of the array
	// O(n)
	int AddFirst(int value)
	{
		if (m_Length >= m_Capacity)
			return -1;
		for (int i = m_Length - 1; i > -1; i--)
		{
			m_Array[i + 1] = m_Array[i];
		}
		m_Array[0] = value;
		m_Length += 1;
		return 1;
	}

	// Add value at the middle of the Array
	// O(n)
	int InsertMiddle(int value, unsigned int index)
	{
		if (m_Length >= m_Capacity)
			return -1;
		for (int i = m_Lengt - 1; i < index - 1; i--)
		{
			m_Array[i + 1] = m_Array[i];
		}
		m_Array[i] = value;
		m_Length += 1;
		return 1;
	}
	// Remove value at the end of the array

	// Remove first 
private:
	const unsigned int m_Capacity = T;
	unsigned int m_Length = 0;
	int m_Array[T];
};

int main()
{
	StaticArray<10> StaticArr;
	StaticArr.Append(1);
	StaticArr.Append(2);
	StaticArr.Append(3);
	StaticArr.AddFirst(10);
	StaticArr.Print();
}