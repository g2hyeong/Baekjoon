#include <iostream>

using namespace std;

const int KMAX = 10001;
const int NMAX = 101;
int dp[KMAX] = { 0, };
int arr[NMAX] = { 0, };
int n, k;

int main() {
	cin >> n >> k;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}

	for (int i = 1; i <= k; i++) {
		for (int j = 1; j <= n; j++) {
			if (i == arr[j]) {
				dp[i] = 1;
				continue;
			}
			if (i > arr[j] && dp[i - arr[j]] != 0)
				if (dp[i] != 0)
					dp[i] = min(dp[i - arr[j]] + 1, dp[i]);
				else
					dp[i] = dp[i - arr[j]] + 1;
		}
	}

	if (dp[k])
		cout << dp[k];
	else
		cout << -1;
}