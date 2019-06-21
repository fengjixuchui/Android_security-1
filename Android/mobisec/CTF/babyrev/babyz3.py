from z3 import *

solver = Solver()

str = [BitVec('%d'%i,8) for i in range(0,6)]
tmp = 'ERNYYL'
for i in range(0,5):
	v2 = str[i]
	if v2 < 'a' or v2 > 'm':
		if v2 >= 'A' and v2 <= 'M':
			v2 = v2 +13
			str[i] = v2
		if v2 >= 'n' and v2 <= 'z':
			v2 = v2 -13
			str[i] = v2
		if v2 < 'L':
			str[i] = v2
		if v2 > 'Z':
			str[i] = v2
	else:
		v2=v2+13
		str[i] = v2

	solver.add(str[i]==tmp[i])

solver.check()
result = solver.model()
 
flag = ''
for i in range(0,5):
    flag += chr(result[str[i]].as_long().real)
print(flag)
