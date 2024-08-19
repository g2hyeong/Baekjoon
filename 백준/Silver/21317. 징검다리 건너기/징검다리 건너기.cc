#include <iostream>

using namespace std;

const int MAX = 999999;
int dp[21];
int dp3[21];
int arr[21][2];
int n, k;

int main() {
	cin >> n;
	for (int i = 1; i < n; i++) {
		cin >> arr[i][0] >> arr[i][1];
	}
	cin >> k;

	for (int i = 0; i <= n; i++) {
		dp[i] = MAX;
		dp3[i] = MAX;
	}

	dp[1] = 0;
	dp[2] = arr[1][0];

	for (int i = 3; i <= n; i++) {
		dp[i] = min(dp[i - 1] + arr[i - 1][0], dp[i - 2] + arr[i - 2][1]);
		dp3[i] = min(min(dp3[i - 1] + arr[i - 1][0], dp3[i - 2] + arr[i- 2][1]), dp[i - 3] + k);
	}

	cout << min(dp3[n], dp[n]);
}