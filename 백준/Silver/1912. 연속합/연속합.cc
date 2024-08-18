#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 100001;

int dp[MAX] = { 0, };
int n, rst;

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> dp[i];
	for (int i = 2; i <= n; i++) {
		dp[i] = max(dp[i], dp[i - 1] + dp[i]);
	}

	rst = *max_element(dp + 1, dp + n + 1);

	cout << rst;
}