s = (42)
m1 = (((42))*60)

m2 = (m1+s)
print (m2)

milha = (10/1.61)
print (milha)

vms = (milha/m2)

print ('{:.3f}' .format(vms),'/milhas por Segundo')

vmm = (vms*60)

print ('{:.3f}' .format (vmm),'/Milhas por Minuto')

vmh = (vmm*60)

print ('{:.3f}' .format(vmh) ,'/Milhas por Hora')
