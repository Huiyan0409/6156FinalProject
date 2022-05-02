def extract(signature):
	words = signature.split() #extract function name after def
	interface = words[1]

	res = ""
	for i in range(len(interface)):
		if interface[i] != '(':
			res += interface[i]
		else:
			break

	return ' '.join(res.split('_'))

print(extract("def load_config(strCsvCnfg, lgcTest=False, lgcPrint=True)"))