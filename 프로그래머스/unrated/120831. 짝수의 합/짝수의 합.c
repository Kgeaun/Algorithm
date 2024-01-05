#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    for(int i = 1; i <= n; i++) {
        if(i % 2 == 0) {
            answer += i;
        }
    }
    return answer;
}

int main() {
    int num1, num2;
    scanf("%d", &num1);
    
    num2 = solution(num1);
    printf("%d", num2);
    return 0;
}