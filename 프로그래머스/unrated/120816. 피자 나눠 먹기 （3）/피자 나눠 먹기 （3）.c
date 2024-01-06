#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int slice, int n) {
    int answer = 0;
    if(n % slice == 0) {
        answer = n / slice;
    }
    else if(n % slice != 0){
        answer = n / slice +1;
    }
    return answer;
}

int main() {
    int num1, num2, result;
    scanf("%d %d", &num1, &num2);
    
    result = solution(num1, num2);
    printf("%d", result);
    return 0;
}