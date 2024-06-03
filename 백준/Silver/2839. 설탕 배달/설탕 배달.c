#include <stdio.h>

int main(){
	int n; scanf("%d", &n);
	int cnt = 0;

	while (1)
	{
		if (n % 5 == 0){
			cnt += n / 5;
			break;
		}
		n -= 3;
		cnt++;
		if (n <= 0) {
			break;
		}
	}
	if (n < 0) {
		printf("-1");
	}
	else printf("%d", cnt);
	
	return 0;
}
