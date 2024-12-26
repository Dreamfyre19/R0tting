import R0tting

while True:
	text = input('Tickle my pickle >> ')
	result, error = R0tting.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)