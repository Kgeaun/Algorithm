import Foundation

func solution(_ n:Int) -> Int {
    if(n % 7 == 0) {
        return n / 7;
    }
    else if(n % 7 != 0) {
        return n / 7 + 1;
    }
    return 0
}