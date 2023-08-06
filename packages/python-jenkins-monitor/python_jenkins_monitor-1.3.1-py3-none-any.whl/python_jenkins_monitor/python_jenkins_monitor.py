import time
import itertools
from datetime import  datetime

def get_next_time(s='* * * * *'):
    if s == '* * * * *':
        return time.time() + 60

    s = s.split(' ')
    for i in range(len(s)):
        fg = ''
        if '/' in s[i]:
            fg = int(s[i].split('/')[1])
            s[i] = s[i].split('/')[0]
        if '-' in s[i]:
            s[i] = list(range(int(s[i].split('-')[0]),int(s[i].split('-')[1])+1))
        elif ',' in s[i]:
            s[i] = [int(j) for j in s[i].split(',')]
        elif '*' in s[i]:
            s[i] = [list(range(0,60)),list(range(0,24)),list(range(1,32)),list(range(1,13)),list(range(1,8))][i]
        else:
            s[i] = [int(s[i])]
        if fg:
            s[i] = list(range(s[i][0],s[i][-1]+1,fg))

    tmp = list(itertools.product(s[0],s[1],s[2],s[3]) )
    all = []
    for i in tmp:
        t = '%s-%s-%s %s:%s:00'%(time.localtime(time.time())[0],i[3],i[2],i[1],i[0])
        try:
            s_t = time.strptime(t, "%Y-%m-%d %H:%M:%S")
        except:
            continue
        mkt = int(time.mktime(s_t))
        if mkt > time.time():
            rq = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mkt))
            dw = datetime.strptime(rq.split(' ')[0],'%Y-%m-%d').isoweekday()
            if dw in s[-1]:
                all.append(mkt)
    all.sort()
    if all:
        return all[0]
    else:
        return None

