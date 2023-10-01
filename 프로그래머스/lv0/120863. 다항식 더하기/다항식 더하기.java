/* 분기 여부
1. polynomial이 하나인지? -> 그대로 return
이제 polynomial 여러개인것만 있음

2. result가 x == 0 || constant == 0 인지? -> 값 있는것만 return
이제 result가 x와 상수 두개 다 있음 " + " 넣어서 String 만들어야함

3. result의 x r계수가 1인지? -> return "x + 상수"
아니면 return "nx + 상수"
*/

class Solution {
    public String solution(String polynomial) {
        int x = 0; // x의 계수
        int constant = 0; // 상수
        if(!polynomial.contains(" + ")) return polynomial;
        String[] poly = polynomial.split(" \\+ "); // 정규식으로 split하기 때문에 escape 문자를 써줘야 함
        for(String str : poly) { // x와 상수 계수 구하기
            if(str.contains("x")) {
                if(str.length() > 1) {
                    str = str.substring(0, str.length() - 1);
                    x += Integer.parseInt(str);
                } else x += 1;
            } else {
                constant += Integer.parseInt(str);
            }
        }
        String answer;
        if(x == 0) {
            return String.valueOf(constant);
        } else {
            if(x == 1) {
                answer = "x";
            } else {
                answer = String.valueOf(x) + "x";
            }
            if(constant != 0) {
                answer += " + " + String.valueOf(constant);
            }
        }
        return answer;
    }
}