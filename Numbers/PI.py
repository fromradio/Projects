k1 = 545140134
k2 = 13591409
k3 = 640320
k4 = 100100025
k5 = 327843840
k6 = 53360
maxn = 100
import math

def computePI(digits):
	if digits > maxn:
		print "maximal decimal digits is set as 100, 100 digits will be computed instead of n"
	# compute the terms used, more than 14 decimal digits per term
	t = int(digits/14) + 1
	S = sum([(-1.0)**n*math.factorial(6*n)*(k2+n*k1)/(math.factorial(n)**3*math.factorial(3*n)*(8*k4*k5)**n) for n in range(0,t)])
	r = (float(k6)*math.sqrt(k3))/S
	return float('{:.{prec}f}'.format(r,prec = digits))