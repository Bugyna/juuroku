import sys

f = open("concept", "rb")

row = 0x0
for b in f.read():
	print(hex(row), end=" | ")
	for i in range(15):
		x = str(hex(b)).split("x")[1]
		if (len(x) == 1): x = "0"+x
		print(x, end=" ")
	row += 0x10
	print(" | ")

f.close()