import pdb

v2='A'
for i in range(0,26):
	
	tmp=''

	if v2 < 'a' or v2 > 'm':
		if v2 >= 'A' and v2 <= 'M':
			tmp = chr(ord(v2) +13)
			
		elif v2 >= 'n' and v2 <= 'z':
			tmp = chr(ord(v2) -13)
			
		elif v2 < 'L':
			tmp = v2
			
		elif v2 > 'Z':
			tmp = v2	
			
	else:
		tmp = chr(ord(v2) +13)
	
	print(v2+ ' [] ' + tmp)

	v2 = chr(ord(v2) +1)

print(v2 + ' ' + tmp)
#'ERNYYL'
ERNYYL

						
#really
	