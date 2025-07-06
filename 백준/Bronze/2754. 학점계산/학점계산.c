#include <stdio.h>
int main() {
	char ch, pm;
	float score = 0;
	scanf("%c%c", &ch, &pm);
	if (ch == 'A') score = 4;
	else if (ch == 'B') score = 3;
	else if (ch == 'C') score = 2;
	else if (ch == 'D') score = 1;
	else score = 0;

	if (pm == '+') score += 0.3;
	else if (pm == '-') score -= 0.3;

	printf("%.1f", score);
}