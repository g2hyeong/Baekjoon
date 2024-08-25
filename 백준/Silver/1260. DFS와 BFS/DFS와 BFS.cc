#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int n, m, v;
vector<vector<int>> graph;
vector<bool> isVisited;


void DFS(int cur);
void BFS(int cur);

int main() {
	cin >> n >> m >> v;
	graph.assign(n + 1, vector<int>(0, 0));
	isVisited.assign(n + 1, false);

	for (int i = 0; i < m; i++) {
		int start, end;
		cin >> start >> end;
		graph[start].emplace_back(end);
		graph[end].emplace_back(start);
	}

	for (int i = 1; i < n+1; i++) {
		sort(graph[i].begin(), graph[i].end());
	}

	DFS(v);

	isVisited.assign(n + 1, false);
	cout << endl;

	BFS(v);
}

void DFS(int cur) {
	isVisited[cur] = true;
	cout << cur << " ";
	for (int i = 0; i < graph[cur].size(); i++) {
		int next = graph[cur][i];
		if (!isVisited[next]) {
			DFS(next);
		}
	}
}

void BFS(int start) {
	queue<int> q;
	q.push(start);
	isVisited[start] = true;

	while (!q.empty()) {
		int cur = q.front();
		q.pop();

		cout << cur << " ";

		for (int i = 0; i < graph[cur].size(); i++) {
			int next = graph[cur][i];
			if (!isVisited[next]) {
				q.push(next);
				isVisited[next] = true;
			}
		}
	}
}

