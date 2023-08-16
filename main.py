from PIL import Image

text = "this is a sample text  and also works with double space."

bg = Image.new(mode="RGBA", size=(1920,1080), color = "white")
im = Image.new(mode="RGBA", size=(20,20), color = "pink")
im2 = Image.new(mode="RGBA", size=(20,20), color = "red")


for i in range(len(text)):

	if text[i].isspace():
		bg.paste(im2,(100+(i*30),100))
	else:
		bg.paste(im,(100+(i*30),100))
bg.show()
