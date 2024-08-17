#include <iostream>

using namespace std;

const int MAX = 50000;
int n;
int dp[MAX] = { 0, };


int main() {
	cin >> n;
	dp[1] = 1;
	for (int i = 2; i <= n; i++) {
		dp[i] = dp[i - 1] + 1;
		for (int j = 1; j * j <= i; j++) {
			dp[i] = min(dp[i], dp[i - j * j] + 1);
		}
	}
	cout << dp[n];
}