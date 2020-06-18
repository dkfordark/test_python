from PIL import Image;
im = Image.open("puppy.jpeg");
print (im.format, im.size, im.mode);
im.show();
