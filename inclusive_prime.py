def inclusive_prime(*args):
	l = len(*args)
	if l==0:
		raise TypeError("Got 0 arguments")
	elif l==1:
		start, stop, step = 0, args[0], 1
	elif l==2:
		start, stop, step = args, 1
	elif l==3:
		start, stop, step = args
	else:
		raise TypeError("Expected maximum 3 arguments got {l}")
	primes = []
	while start <= stop:
		f = 1
		x = 1
		while x <= start:
			if start % x == 0 :
				f = 0
				break
			x+=1
		if f == 1:
			primes.append(start)
		else:
			continue
		start += step
	print(primes)


def main():
	inclusive_prime(3,15,2)


if __name__ == '__main__':
	main()