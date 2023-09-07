/*pseudocode
n % slice == 0이면 answer는 n / slice
아니면 n/slice + 1
*/

class Solution {
    public int solution(int slice, int n) {
        if(n % slice == 0) {
            return n / slice;
        }
        return n/slice + 1;
    }
}