class Solution {
    public int solution(int n) {
        int num1 = 0;
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                num1 += i;
            }
        }
        return num1;
    }
}