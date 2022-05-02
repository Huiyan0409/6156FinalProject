def extract(signature):
	words = signature.split() #extract function name after def
	interface = words[1]

	res = ""
	for i in range(len(interface)):
		if interface[i] != '(':
			res += interface[i]
		else:
			break

	return res.split('_')

print(extract("def do_transform(self, v=<NUM_LIT:1>):"))
