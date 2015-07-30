# no good way as pi to compute N-th digits of e
# however, 20 steps of taylor expand assures about 50 digits of e

import math
#compute e
e = sum([1.0/math.factorial(n) for n in range(0,20)])
maxn = 50

def computeE(digits):
	return float('{:.{prec}f}'.format(e,prec=digits))

if __name__ == '__main__':
	while True:
		s = raw_input("How many digits do u need")
		try:
			digits = int(s)
			if digits>maxn:
				print "Enter a number smaller than",maxn
			elif digits<0:
				print "Enter a nonnegtive number"
			print '{:.{prec}f}'.format(computeE(digits),prec=digits)
		except ValueError:
			print "Enter a nonnegtive number"