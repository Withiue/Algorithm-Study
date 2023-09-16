/*
letter를 공백 기준으로 split하고 배열에 매핑하기
답 봤는데도 for문 돌아가는게 헷갈림 그림 그려가면서 생각하기
*/
class Solution {
    public String solution(String letter) {
        String[] morse = { 
            ".-","-...","-.-.","-..",".","..-.",
            "--.","....","..",".---","-.-",".-..",
            "--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-",
            "-.--","--.."
        };
        
        String[] letters = letter.split(" ");
        StringBuilder answer = new StringBuilder();
        
        for(String word : letters) {
            for(int i = 0; i < morse.length; i++) {
                if(word.equals(morse[i])) {
                    answer.append(Character.toString(i+'a'));
                }
            }
        }
        return answer.toString(); //StrintBuilder를 String으로 변환
    }
}