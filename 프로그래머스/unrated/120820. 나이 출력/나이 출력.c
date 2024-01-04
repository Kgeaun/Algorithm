#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int age) {
    int answer = 0;
    answer = 2023 - age;
    return answer;
}

int main() {
    int x, sum;
    scanf("%d", &x);
    
    sum = solution(x);
    printf("%d", sum);
    return 0;
}