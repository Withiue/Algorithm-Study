/*
* 1. num1을 num2로 나눈다.(이때 둘 중 하나 이상을 double로 형변환한다.)
* 2. 1의 값에 1000을 곱한다.
* 3. 2의 값을 int로 강제 형변환한다.
* 4. 3의 값을 return한다.
*/

class Solution {
    public int solution(int num1, int num2) {
        double divide = (double) num1 / num2; // num1을 double로 형변환한다.
        divide *= 1000;
        int answer = (int) divide;
        return answer;
    }
}