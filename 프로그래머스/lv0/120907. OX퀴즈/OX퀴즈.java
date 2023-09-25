class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        for(int i = 0; i < quiz.length; i++) {
            String[] splitQuiz = quiz[i].split(" ");
            int X = Integer.parseInt(splitQuiz[0]);
            int Y = Integer.parseInt(splitQuiz[2]);
            int Z = Integer.parseInt(splitQuiz[4]);
            if(splitQuiz[1].equals("+")) {
                if(X + Y == Z) {
                    answer[i] = "O";
                } else answer[i] = "X";
            } else {
                if(X - Y == Z) {
                    answer[i] = "O";
                } else answer[i] = "X";
            }
        }
        return answer;
    }
}