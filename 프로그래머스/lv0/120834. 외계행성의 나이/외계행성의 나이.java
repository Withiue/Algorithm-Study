class Solution {
    public String solution(int age) {
        String answer = "";
        String strAge = Integer.toString(age); // age를 string으로 바꿈
        for(int i = 0; i < strAge.length(); i++) { // strAge를 차례대로 검사하면서 알파벳으로 바꿔서 answer에 넣음
            answer += (char)(strAge.charAt(i) + 49);
            
        }
        return answer;
    }
}

/*
처음에 age를 문자열로 반환할 생각을 못하고 int 자체로 사용할 생각만 하다보니
점점 식이 복잡해졌다. 자료형의 틀에 갇히지 말기
*/