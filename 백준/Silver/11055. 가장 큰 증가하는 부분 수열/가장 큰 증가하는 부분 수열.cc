#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

const int MAX = 1001;
int n, ptr = 0, tmp = -1, sum = -1;
bool flag;
int arr[MAX] = { 0, };
vector<vector<int>> dp(MAX, vector<int>(0, 0));

int getSum(std::vector<int> const& vec) {
	if (vec.empty()) {
		return 0;
	}
	return std::accumulate(vec.begin(), vec.end(), 0);
}


int main() {
	cin >> n;

	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
	}

	for (int i = 1; i <= n; i++) {
		tmp = -1;
		flag = false;
		dp[i].push_back(arr[i]);
		for (int j = 1; j < i; j++) {
			if (arr[i] > arr[j]) {
				flag = true;
				if (getSum(dp[j]) > tmp) {
					tmp = getSum(dp[j]);
					ptr = j;
				}
			}
		}
		if(flag)
			for (int k = 0; k < (int)dp[ptr].size(); k++)
				dp[i].push_back(dp[ptr][k]);
		/*
		for (int k = 0; k < (int)dp[i].size(); k++) {
			cout << dp[i][k] << " ";
		}
		cout << "\n";
		*/
		
	}

	for (int i = 0; i < (int)dp.size(); i++) {
		sum = max(sum, getSum(dp[i]));
	}

	cout << sum;

}