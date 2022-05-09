q = chr(34)
c = chr(44)
list = [
"q = chr(34)",
"c = chr(44)",
"list = [",
"]",
"for i in range(3):",
"	print(list[i])",
"for i in list:",
"	print(q + i + q + c)",
"print()",
"for i in range(3,11):",
"	print(list[i])",

]
for i in range(3):
	print(list[i])
for i in list:
	print(q + i + q + c)
print()
for i in range(3,11):
	print(list[i])
