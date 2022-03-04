import math

n = 78437839
l = math.ceil(math.log(n)/math.log(10))
i = 1
o = 0
while n > 0:
	d = n % (10)
	n -= d
	n /= 10
	print(d)
	o += d * (10**(l-i))
	i += 1
print(o)
	
