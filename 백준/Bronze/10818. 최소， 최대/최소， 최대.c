#include <stdio.h>

int main()
{
int a, b,c=0, max = -1000000, o = 1000000;
scanf("%d", &a);

for (int i = 1;i <= a;i++)
{
scanf("%d", &b);
if (max < b)
{
max = b;
}
if (o > b)
{
o = b;
}
}
printf("%d %d",o,max);
return 0;
}