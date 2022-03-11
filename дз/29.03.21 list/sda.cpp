
#include <iostream>
using namespace std;
int main()
{
	float b;
	float h;
	float s;
	cin >> b >> h;
	s = 0.5 * b * h;
	cout << s;
	if (h == b) {
		cout << h + b;
	}
	else {
		cout << h - b;
	}
}
