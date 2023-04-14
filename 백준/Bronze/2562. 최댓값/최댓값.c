#include <stdio.h>

int main()
{
int a = 9, count=0,max=0, b;

for (int i = 1; i <= a;i++)
{
scanf("%d", &b);
if (max < b) {
max = b;
count = i;

}
}
printf("%d\n%d\n", max, count);
return 0;
}