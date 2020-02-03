f = open("image.ppm", "w")

import random
f.write("P3 \n500 500 \n255 \n")

length = 0
r = 255
g = 0
b = 80
r2 = 255
g2 = 22
b2 = 200
string = str()
split = 400

while (length < 500):
	width = 0
	while (width < 500):
		if (length > 370):
			string += "255 228 181 "
		elif (width < split):
			string += str(r) + " " + str(g) + " " + str(b) + " "
		else:
			string += str(r2) + " " + str(g2) + " " + str(b2) + " "
		width += 1
	g = (g + 1) 
	r2 = (r2 - 1) 
	g2 = (g2 + 1)
	string += "\n"
	length += 1
	split -= random.uniform(0, 1.5)

f.write(string)
f.close()