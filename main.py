from PIL import Image

text = "this is a sample text  and also works with double space. 12345 121333 1214 21313 . can i  havea  alot more text in this to make it any more vialle to scan a nd paste hand wrting biiiiiiiiiiii. fjdnd"

bg = Image.new(mode="RGBA", size=(595, 842), color = "white")
im = Image.new(mode="RGBA", size=(10,10), color = "pink")
im2 = Image.new(mode="RGBA", size=(10,10), color = "red")

line = 0
margin = 10
y = 1
x = 0

for i in range(len(text)):

	

	if text[i].isspace():
		bg.paste(im2,(margin+(x*10),margin+(y*20)))
		x+=1
	else:
		bg.paste(im,(margin+(x*10),margin+(y*20)))
		x+=1
	
	if margin+(x*10) >= 595-margin:
		x = 0
		y+=1
	
		
bg.show()
