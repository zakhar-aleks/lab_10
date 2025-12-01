with open("test.txt", "w") as f:
	for i in range(1, 10):
		f.write("a" * i + "\n")