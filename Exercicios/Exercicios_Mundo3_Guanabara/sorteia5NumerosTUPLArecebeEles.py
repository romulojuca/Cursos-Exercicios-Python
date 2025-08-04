from random import randint, sample

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
ma = n[0]
me = n[0]

print(f'{n}')

if n[1] > ma:
    ma = n[1]
if n[2] > ma:
    ma = n[2]
if n[3] > ma:
    ma = n[3]
if n[4] > ma:
    ma = n[4]

if n[1] < me:
    me = n[1]
if n[2] < me:
    me = n[2]
if n[3] < me:
    me = n[3]
if n[4] < me:
    me = n[4]

print(f'Maior {ma}')
print(f'Menor {me}')
