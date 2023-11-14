#include <stdio.h>

int main() {
    int a, num1, num2;
    scanf("%d", &a);
    for(int i = 1; i <= a; i++) {
        scanf("%d %d", &num1, &num2);
        printf("%d\n", num1 + num2);
    }
    return 0;
}