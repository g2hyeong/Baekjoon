#include <iostream>

using namespace std;

const int MAX = 1003;
int dp[MAX] = { 0, };
int n;

int main() {
	cin >> n;

	dp[1] = 1;
	dp[2] = 3;

	for (int i = 3; i <= n; i++) {
		dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007;
	}

	cout << dp[n];
}