numero = int(input('Digite um numero entre 0 e 20: '))

nums = ('zero', 'um', 'dois', 'trez', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeceis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    if numero < 0 or numero > 20:
        numero = int(input('Tente novamente!... Digite um numero: '))
    else:
        print(nums[numero])
        break
