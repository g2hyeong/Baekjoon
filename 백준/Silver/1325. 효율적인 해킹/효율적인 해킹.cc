#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> graph;
vector<bool> isVisited;
vector<pair<int, int>> rst;
int n, m;
int cnt;

void DFS(int cur);

int main() {
	cin >> n >> m;

	graph.assign(n + 1, vector<int>(0, 0));

	for (int i = 0; i < m; i++) {
		int start, end;
		cin >> start >> end;
		graph[end].emplace_back(start);
	}

	for (int i = 1; i <= n; i++) {
		cnt = 0;
		isVisited.assign(n + 1, false);
		DFS(i);
		if (rst.empty())
			rst.emplace_back(make_pair(i, cnt));
		else {
			if (rst.front().second == cnt) {
				rst.emplace_back(make_pair(i, cnt));
			}
			else if (rst.front().second < cnt) {
				rst.clear();
				rst.emplace_back(make_pair(i, cnt));
			}
		}
	}
	sort(rst.begin(), rst.end());
	for (int i = 0; i < rst.size(); i++)
		cout << rst[i].first << " ";
}

void DFS(int cur) {
	cnt++;
	isVisited[cur] = true;
	for (int i = 0; i < graph[cur].size(); i++) {
		int next = graph[cur][i];
		if (!isVisited[next]) {
			DFS(next);
		}
	}
}