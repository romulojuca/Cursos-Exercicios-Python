N = int(input('Quantidade de segundos: '))
r = m = n = s = h = 0

if N >= 3600:
    h = N / 3600
    r = (h * 3600) - (int(h) * 3600)
    if r >= 60:
        m = r / 60
        r = (m * 60) - (int(m) * 60)
        if r >= 1:
            s = r
elif N >= 60:
    m = N / 60
    r = (m * 60) - (int(m) * 60)
    if r >= 1:
        s = r
elif N >= 1:
    s = N
    m = 0

print('{}:{}:{}'.format(int(h), int(m), int(s)))
