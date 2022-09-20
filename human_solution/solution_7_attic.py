__author__ = 'TAPOPADMA'


class Path:
    path = ''

    def __init__(self, _path):
        self.path = _path

    def NoOfDays(self):
        days = 0
        S = self.path
        prev_floor = S[0]
        cnt = int(S[0] == '.')
        max_cnt = 0
        for cur_floor in S[1:]:
            if cur_floor == prev_floor:
                if cur_floor == '.':
                    cnt += 1
            else:
                if cur_floor == '.':
                    cnt = 1
                else:
                    if cnt > max_cnt:
                        days += 1
                        max_cnt = cnt
            prev_floor = cur_floor
        if S[-1] == '.':
            if cnt > max_cnt:
                days += 1
        return days

T = int(input())
while T:
    T -= 1
    p = input()
    path = Path(p)
    print(path.NoOfDays())