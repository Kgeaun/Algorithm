#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int n) {
    int answer = 0;
    if(n % 7 == 0) {
        answer = n / 7;
    }
    else if(n % 7 != 0) {
        answer = n / 7 + 1;
    }
    return answer;
}

int main() {
    int num1, result;
    scanf("%d", & num1);
    result = solution(num1);
    
    printf("%d", result);
    return 0;
}