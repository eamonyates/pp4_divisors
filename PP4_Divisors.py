def divisor():
	number = int(input("Please enter a number: "))
	full_list = range(2, number)
	div_list = []
	for num in full_list:
		if number % num == 0:
			div_list.append(num)
		else:
			continue
	print (div_list)


if __name__ == "__main__":
	divisor()
