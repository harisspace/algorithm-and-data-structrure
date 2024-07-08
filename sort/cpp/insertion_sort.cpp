#include <iostream>
#include <vector>

void InsertionSort(int* a, size_t length)
{
	for (int i = 1; i < length; i++)
	{
		int j = i - 1;
		while (j >= 0 && a[j + 1] < a[j])
		{
			int temp = a[j];
			a[j] = a[j + 1];
			a[j + 1] = temp;
			j--;
		}
	}
}

int main()
{
	int arr[10] = { 5,3,6,2,7,4,1 };
	InsertionSort(arr, 7);
	for (int i = 0; i < 7; i++)
	{
		std::cout << arr[i] << "\n";
	}
}