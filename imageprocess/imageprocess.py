from PIL import Image,ImageFilter,ImageEnhance 

img=Image.open('./img/4.1 charmander.jpg')
print(img)
filter_img=img.filter(ImageFilter.BLUR) #filter to blur
print(img.format)
print(img.size)
print(img.mode)
print(img.palette)
filter_img.save("blur.png","png")
filter_img=img.filter(ImageFilter.GaussianBlur) #filter to gaussianblur
filter_img.save("gaussinblur.png","png")

filter_img=img.convert("L")#convert to grayscale
filter_img=filter_img.rotate(180)
resize=img.resize((400,600))
filter_img.save("grey.png", "png") 
crop=filter_img.crop((100,100,400,400))

en=ImageEnhance.Contrast(img)
#en.enhance(2.3).show(" more contrast")
crop.save("c.png", "png") 
en=ImageEnhance.Color(img) #enhancing images color,contrast,brightness,sharpness
#en.enhance(2.3).show("more color")

resize.save("r.png", "png") 
#filter_img.show()

img.thumbnail((200,200))
img.save('i.jpg')

print(img.size)