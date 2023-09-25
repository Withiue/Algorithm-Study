class Solution {
    public int solution(String my_string) {
        String[] array = my_string.split(" ");
        int answer = Integer.parseInt(array[0]);
        for(int i = 1; i < array.length - 1 ; i += 2) {
            if(array[i].equals("+")) {
                answer += Integer.parseInt(array[i+1]);
            } else {
                answer -= Integer.parseInt(array[i+1]);
            }
        }
        return answer;
    }
}