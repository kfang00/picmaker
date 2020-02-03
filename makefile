all: picmaker.py 
	python3 picmaker.py
	convert image.ppm image.png
	display image.png  
	
