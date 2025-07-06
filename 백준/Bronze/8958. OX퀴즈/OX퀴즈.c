#include <stdio.h>
int main() {
	int t; scanf("%d", &t);
	char ch[82];
	while (t--) {
		int total = 0;
		scanf("%s", &ch);
		int idx = 0, score = 0;
		while (ch[idx] != '\0') {
			if (ch[idx] == 'X') score = 0;
			else score++;
			total += score;
			idx++;
		}
		printf("%d\n", total);
	}
}