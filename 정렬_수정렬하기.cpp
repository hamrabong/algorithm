#include <iostream>
using namespace std;

int main() {
	int temp, N, num[1000];
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}

	for (int j = 0; j < N; j++) {
		for (int k = 0; k < N - 1; k++) {
			if (num[k] > num[k + 1]) {
				temp = num[k];
				num[k] = num[k + 1];
				num[k + 1] = temp;
			}
		}
	}

	for (int i = 0; i < N; i++) {
		cout << num[i] << endl;
	}
	return 0;
}