class Solution {
    public int solution(int num, int k) {
        String str = String.valueOf(num);
        for(int i = 0; i < str.length(); i++) {
            if(str.charAt(i) == (char) (k + '0')) return i+1; // int + 숫자 아스키 코드 시작점(0) -> char로 형변환 => int를 char로 변환 가능
        }
        return -1;
    }
}