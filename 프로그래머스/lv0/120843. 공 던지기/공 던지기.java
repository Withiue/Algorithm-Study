class Solution {
    public int solution(int[] numbers, int k) {
        return numbers[2 * (k-1) % numbers.length]; // numbers[0 + 2 * (k-1) % numbers.length], index 0 부터 시작해서 k-1번 던졌을때 받은 사람을 구하기
    }
}