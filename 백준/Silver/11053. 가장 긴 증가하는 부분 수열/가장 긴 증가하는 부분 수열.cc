#include <iostream>

using namespace std;

const int MAX = 1001;
int arr[MAX] = { 0, };
int dp[MAX] = { 0, };
int n, ptr = 1, rst = -1;

int main() {
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}
	for (int i = 1; i <= n; i++) {
		dp[i] = 1;
		for (int j = 1; j < i; j++) {
			if(arr[i] > arr[j])
				dp[i] = max(dp[j] + 1, dp[i]);
		}
		rst = max(rst, dp[i]);
	}

	cout << rst;
}