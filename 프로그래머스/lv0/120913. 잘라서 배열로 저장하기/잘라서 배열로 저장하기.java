class Solution {
    public String[] solution(String my_str, int n) {
        int size = (my_str.length() % n) == 0 ? (my_str.length() / n) : (my_str.length() / n) + 1; // 필요한 크기만큼 할당
        String[] answer = new String[size];
        for(int i = 0; i < size; i++) {
            int startIndex = i * n;
            int endIndex = startIndex + n;
            if(i == size - 1) { // 마지막 루프면
                answer[i] = my_str.substring(startIndex); // 나머지 다 넣기
            } else answer[i] = my_str.substring(startIndex, endIndex); //핵심!
        }
        return answer;
    }
}