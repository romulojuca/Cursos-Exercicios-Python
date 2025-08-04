from time import sleep
num = ()
def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...', flush=True)
    sleep(0.5)
    m = 0
    print('Foram informados os valores: ', end='')
    for p in num:
        if p == 0:
            m = p
        if p > m:
            m = p
        print(f'{p} ', end='')
    print()
    print(f'Foram informados {len(num)} valores!')
    print(f'O maior valor foi {m}')


maior(10, 1, 50, 90, 17)
maior(70, 10, 50, 47, 10, 787)
