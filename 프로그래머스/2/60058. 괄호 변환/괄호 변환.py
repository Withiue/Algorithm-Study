def solution(p):

    

    # 올바른 괄호 문자열인지 확인

    def is_correct(s):

        cnt = 0

        

        for ch in s:

            if ch == '(':

                cnt += 1

            else:

                cnt -= 1

            

            # 닫는 괄호가 먼저 많아지면 잘못된 문자열

            if cnt < 0:

                return False

        

        return True

    

    

    # 문제에서 주어진 변환 과정

    def convert(w):

        

        # 1. 빈 문자열이면 그대로 반환

        if w == '':

            return ''

        

        # 2. w를 u, v로 분리

        cnt = 0

        

        for i in range(len(w)):

            if w[i] == '(':

                cnt += 1

            else:

                cnt -= 1

            

            # 처음으로 괄호 개수가 같아지는 지점

            if cnt == 0:

                u = w[:i + 1]

                v = w[i + 1:]

                break

        

        # 3. u가 올바른 괄호 문자열이면

        if is_correct(u):

            return u + convert(v)

        

        # 4. u가 올바른 괄호 문자열이 아니라면

        else:

            result = '('

            result += convert(v)

            result += ')'

            

            # u의 첫 번째, 마지막 문자 제거

            u = u[1:-1]

            

            # 나머지 괄호 방향 뒤집기

            for ch in u:

                if ch == '(':

                    result += ')'

                else:

                    result += '('

            

            return result

    

    return convert(p)