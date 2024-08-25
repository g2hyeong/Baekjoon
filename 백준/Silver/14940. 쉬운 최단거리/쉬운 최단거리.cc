#include <iostream>
#include <queue>

using namespace std;

int graph[1002][1002] = { 0 };
int isVisited[1002][1002] = { 0 };

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { -1, 0, 1, 0 };

queue<pair<int,int>> q;

int n, m;
int startX, startY;

void BFS(int x, int y);

int main() {
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> graph[i][j];
			if (graph[i][j] == 2) {
				startX = i;
				startY = j;
			}
		}
	}

	BFS(startX, startY);

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			if (graph[i][j] == 0)
				cout << 0 << " ";
			else
				cout << isVisited[i][j] - 1 << " ";
		}
		cout << "\n";
	}
}

void BFS(int x, int y) {
	q.push(make_pair(x, y));
	isVisited[x][y] = 1;

	while (!q.empty()) {
		int tmpX = q.front().first;
		int tmpY = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int nextX = tmpX + dx[i];
			int nextY = tmpY + dy[i];
			if (nextX >= 1 && nextX <= n && nextY >= 1 && nextY <= m) {
				if (!isVisited[nextX][nextY] && graph[nextX][nextY] != 0) {
					isVisited[nextX][nextY] = isVisited[tmpX][tmpY] + 1;
					q.push(make_pair(nextX, nextY));
				}
			}
		}
	}
}