a = 80000
a_cresc = 0.03
b = 200000
b_cesc = 0.015
cont = 0

while a < b:
    a = a + (a * a_cresc)
    b = b + (b * b_cesc)
    cont += 1

print(
    f"Serão necessario {cont} anos! E o país A terá {int(a)} habitantes, enquanto o B terá {int(b)}")
