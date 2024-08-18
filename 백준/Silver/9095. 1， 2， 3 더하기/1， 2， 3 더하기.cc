#include <iostream>

using namespace std;

const int MAX = 12;

int dp[MAX] = { 0, 1, 2, 4, };
int n, cnt;

int main() {
	cin >> cnt;
	for (int i = 4; i <= 11; i++) {
		dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
	}

	for (int i = 0; i < cnt; i++) {
		cin >> n;
		cout << dp[n] << "\n";
	}
}