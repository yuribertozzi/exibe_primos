def primos(x):

	divisor = 2

	primalidade = True

	while divisor < n and primalidade == True:

		if n % divisor == 0:

			primalidade = False

		divisor = divisor + 1

	if primalidade == True and n != 1:

		return True
	
	else:

		return False

limite = int(input("Limite máximo: "))

n = 2

while n <= limite:

    if primos(n):

        print(n, end=", ")

    n = n + 1
