#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> graph;
vector<bool> isVisited;
vector<int> parent;

int n;

void DFS(int cur);

int main() {
	cin >> n;
	
	graph.assign(n + 1, vector<int>(0, 0));
	isVisited.assign(n + 1, false);
	parent.assign(n + 1, 0);

	for (int i = 0; i < n - 1; i++) {
		int start, end;
		cin >> start >> end;
		graph[start].emplace_back(end);
		graph[end].emplace_back(start);
	}

	DFS(1);

	for (int i = 2; i <= n; i++)
		cout << parent[i] << "\n";
}

void DFS(int cur) {
	isVisited[cur] = true;
	for (int i = 0; i < graph[cur].size(); i++) {
		int next = graph[cur][i];
		if (!isVisited[next]) {
			parent[next] = cur;
			DFS(next);
		}
	}
}