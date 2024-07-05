#include <iostream>
#include "vector.h"
#include <string>

struct Vector3
{
	float x = 0.0f, y = 0.0f, z = 0.0f;

	Vector3()
	{
	}

	~Vector3()
	{
		std::cout << "Destroy" << std::endl;
	}

	Vector3(float scalar)
		: x(scalar), y(scalar), z(scalar)
	{
	}

	Vector3(float x, float y, float z)
		: x(x), y(y), z(z)
	{
	}

	Vector3(const Vector3& other)
	{
		std::cout << "Copy" << std::endl;
	}

	Vector3(Vector3&& other)
	{
		std::cout << "Move" << std::endl;
	}

	Vector3& operator=(Vector3&& other)
	{
		std::cout << "Move" << std::endl;
		x = other.x;
		y = other.y;
		z = other.z;
		return *this;
	}
	
	Vector3& operator=(const Vector3& other)
	{
		std::cout << "Copy" << std::endl;
		x = other.x;
		y = other.y;
		z = other.z;
		return *this;
	}
};

template <typename T>
void PrintVector(const Vector<T>& vector)
{
	for (size_t i = 0; i < vector.Size(); i++)
	{
		std::cout << vector[i] << std::endl;
	}

	std::cout << "----------------------------------\n";
}

template <>
void PrintVector(const Vector<Vector3>& vector)
{
	for (size_t i = 0; i < vector.Size(); i++)
	{
		std::cout << vector[i].x << vector[i].y << vector[i].z << std::endl;
	}

	std::cout << "----------------------------------\n";
}

int main()
{
	Vector<Vector3> vector;
	vector.PushBack(Vector3(1.0f));
	vector.PushBack(Vector3(1.0f, 2.0f, 3.0f));
	vector.PushBack(Vector3());

	PrintVector(vector);

	std::cin.get();
}