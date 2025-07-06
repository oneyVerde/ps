#include <stdio.h>
int main() {
	int n, m; scanf("%d %d", &n, &m);
	int arrA[101][101] = {0}, arrB[101][101] = {0};
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			scanf("%d", &arrA[i][j]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			scanf("%d", &arrB[i][j]);
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			printf("%d ", arrA[i][j] + arrB[i][j]);
		printf("\n");
	}
}