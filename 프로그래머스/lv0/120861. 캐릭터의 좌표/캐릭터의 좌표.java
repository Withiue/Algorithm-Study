/*임시로 실행한다음 board의 크기를 벗어나면 실행 취소하고 continue 하기*/
class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[2];
        int temp = 0;
        for(String key : keyinput) {
            if(key.equals("up")) {
                temp = answer[1] + 1;
                if(Math.abs(temp) > board[1] / 2) continue;
                answer[1] = temp;
            }
            if(key.equals("down")) {
                temp = answer[1] - 1;
                if(Math.abs(temp) > board[1] / 2) continue;
                answer[1] = temp;
            }
            if(key.equals("left")) {
                temp = answer[0] - 1;
                if(Math.abs(temp) > board[0] / 2) continue;
                answer[0] = temp;
            }
            if(key.equals("right")) {
                temp = answer[0] + 1;
                if(Math.abs(temp) > board[0] / 2) continue;
                answer[0] = temp;
            }
            
        }
        return answer;
    }
}