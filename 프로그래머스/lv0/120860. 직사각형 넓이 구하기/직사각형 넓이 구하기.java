class Solution {
    public int solution(int[][] dots) {
        int width = 0;
        int height = 0;
        int x = dots[0][0]; // x 초기값 설정
        int y = dots[0][1]; // y 초기값 설정
        for(int i = 1; i < dots.length; i++) {
            if (x != dots[i][0]) width = Math.abs(x - dots[i][0]);
            if (y != dots[i][1]) height = Math.abs(y - dots[i][1]);
        }
        return width * height;
    }
}