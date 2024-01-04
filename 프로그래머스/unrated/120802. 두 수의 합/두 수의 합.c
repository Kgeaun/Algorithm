#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num1, int num2) {
    int answer = 0;
    answer = num1 + num2;
    return answer;
}

int main() {
    int x, y, sum;
    scanf("%d %d", &x, &y);
    
    sum = solution(x,y);
    printf("%d", sum);
    return 0;
}