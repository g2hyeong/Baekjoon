#include <iostream>

using namespace std;

const int SIZE = 101;
long arr[SIZE][SIZE] = { 0, };
long dp[SIZE][SIZE] = { 0, };
int n;

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (i == 0 && j == 0)
				dp[i][j] = 1;
			else if (i == 0 && j != 0) {
				for (int k = 1; k <= j; k++) {
					if (arr[i][j - k] == k)
						dp[i][j] += dp[i][j-k];
				}
			}
			else if (i != 0 && j == 0) {
				for (int k = 1; k <= i; k++) {
					if (arr[i - k][j] == k)
						dp[i][j] += dp[i - k][j];
				}
			}
			else {
				for (int k = 1; k <= j; k++) {
					if (arr[i][j - k] == k)
						dp[i][j] += dp[i][j - k];
				}
				for (int k = 1; k <= i; k++) {
					if (arr[i - k][j] == k)
						dp[i][j] += dp[i - k][j];
				}
			}
		}
	}

	cout << dp[n - 1][n - 1];

}