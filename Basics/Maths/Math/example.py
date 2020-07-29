# refer to this problem: https://www.hackerrank.com/challenges/find-angle/problem
import math
ab=float(input())
bc=float(input())
ac=math.sqrt(math.pow(ab,2)+math.pow(bc,2))
mc=ac/2
# °
bm=math.pow(bc,2)+math.pow(mc,2)-(2*(bc*mc)*(bc/ac))
bm=math.sqrt(bm)
cos_=math.pow(bm,2)+math.pow(bc,2)-math.pow(mc,2)
cos_/=2*bc*bm
deg=math.acos(cos_)
deg=math.degrees(deg)
estimate=int(deg)+0.5
if estimate>deg:
    print(str(math.floor(deg))+'°')
else:
    print(str(math.ceil(deg))+'°')    