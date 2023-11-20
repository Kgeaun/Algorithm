int main() {
    long long n, m;

    scanf("%lld %lld", &n, &m);
    if(n - m < 0) printf("%lld", (n - m) * -1);
    else printf("%lld", n-m);
    return 0;
}