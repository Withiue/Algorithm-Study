/*
HashMap으로 푸려다 어려워서 다른 방식으로 풀었다.
*/
class Solution {
    public String solution(String rsp) {
        String answer = "";
        for(int i = 0; i < rsp.length(); i++) {
            if(rsp.split("")[i].equals("2")) {
                answer += "0";
            } else if(rsp.split("")[i].equals("0")) {
                answer += "5";
            } else answer += "2";
        }
        return answer;
    }
}