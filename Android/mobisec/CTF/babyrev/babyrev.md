# babyrev
本题目解决 FlagChecker 就行

> flag = ''

## part 1

* if(!arg11.startsWith("MOBISEC{")) 

> flag = "MOBISEC{" + string

## part 2

* if(new StringBuilder(arg11).reverse().toString().charAt(0) != 125) 

> flag = "MOBISEC{" + string + "}"

## part 3

* if(arg11.length() != 35)

> len(flag) = 35

## part 4

* arg11.toLowerCase().substring(v2).startsWith("this_is_")

> flag = "MOBISEC{" + "this_is_" + string + "}"
> flag = "MOBISEC{this_is_" + string + "}"

## part 5

* new StringBuilder(arg11).reverse().toString().toLowerCase().substring(1).startsWith(arg10.getString(2131427368)

2131427368 -> "last_past"

> flag = "MOBISEC{this_is_" + string + "tsap_tsal" + "}"

> flag = "MOBISEC{this_is_" + string + "tsap_tsal}"

## part 6 

* 1. arg11.charAt(17) == 95

* 2. arg11.charAt(((int)((((double)FlagChecker.getY())) * Math.pow(((double)FlagChecker.getX()), ((double)FlagChecker.getY()))))) != arg11.charAt((((int)Math.pow(Math.pow(2, 2), 2))) + 1)) 

* 3. FlagChecker.bam(arg11.toUpperCase().substring(FlagChecker.getY() * FlagChecker.getX() * FlagChecker.getY(), ((int)(Math.pow(((double)FlagChecker.getZ()), ((double)FlagChecker.getX())) - 1)))).equals("ERNYYL")) 

解密过来

'''
FlagChecker.bam(arg11.toUpperCase().substring(18, 24)).equals("ERNYYL")) 

str=flag[18:24)
really
for(i=0;i<=6;++i){
	v2 = str[i]
	if v2 < 'a' || v2 > 'm':
		if(v2 >= 'A' && v2 <= 'M')
			v2 = v2 +13
			v0+=v2
		if(v2 >= n && v2 <= z )
			v2 = v2 -13
			v0+=v2
		if(v2 < 'L')
			v0+=v2
		if(v2 > 'Z')
			v0+=v2
	else
		v2=v2+13
		v0+=v2
} 
'''

* 4. v4 = 16 arg11.toLowerCase().charAt(v4) = 97

* 5. arg11.charAt(16) = arg11.charAt(26)

* 6. arg11.toUpperCase().charAt(25) != arg11.toUpperCase().charAt(26) + 1)

> flag = 
"MOBISEC{this_is_" + "a" + "_" +"really" +"_"+ "ba" + "tsap_tsal}"

> flag = 
"MOBISEC{this_is_a_really_batsap_tsal}"

## part 7 

* arg11.substring(v2, arg11.length() - 1).matches(FlagChecker.getR())


> flag = MOBISEC{tHiS_Is_a_rEaLlY_Basic_rev}

MOBISEC{tHiS_Is_a_rEaLlY_BaSiC_ReV}
MOBISEC{ThIs_iS_A_ReAlLy_bAsIc_rEv}
	   '01010101010101010101010101'






